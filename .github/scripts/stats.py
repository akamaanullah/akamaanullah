"""Generates assets/stats.svg (orange themed GitHub stats card) from the GitHub API."""
import os, json, datetime, collections, urllib.request
from xml.sax.saxutils import escape as esc

USER = os.environ.get("GH_USER", "akamaanullah")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = os.environ.get("STATS_OUT", "assets/stats.svg")
MONO = "'Fira Code','JetBrains Mono','SF Mono',Consolas,Menlo,monospace"
SANS = "'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif"


def api(path):
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-stats")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def collect():
    data = {"repos": 0, "stars": 0, "followers": 0, "commits": None, "langs": []}
    try:
        u = api(f"/users/{USER}")
        data["repos"], data["followers"] = u["public_repos"], u["followers"]
        repos, page = [], 1
        while True:
            chunk = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
            repos += chunk
            if len(chunk) < 100:
                break
            page += 1
        own = [r for r in repos if not r["fork"]]
        data["stars"] = sum(r["stargazers_count"] for r in own)
        langs = collections.Counter()
        for r in own:
            try:
                for k, v in api(f"/repos/{USER}/{r['name']}/languages").items():
                    langs[k] += v
            except Exception:
                pass
        total = sum(langs.values()) or 1
        data["langs"] = [(k, v * 100 / total) for k, v in langs.most_common(6)]
    except Exception as e:
        print("stats error:", e)
    try:
        data["commits"] = api(f"/search/commits?q=author:{USER}&per_page=1")["total_count"]
    except Exception:
        pass
    return data


def render(d):
    tiles = [
        ("REPOSITORIES", d["repos"]),
        ("STARS EARNED", d["stars"]),
        ("FOLLOWERS", d["followers"]),
        ("TOTAL COMMITS", d["commits"] if d["commits"] is not None else "-"),
    ]
    t = ""
    for i, (lab, val) in enumerate(tiles):
        x = 24 + (i % 2) * 232
        y = 24 + (i // 2) * 132
        t += f'''<g>
<rect x="{x}" y="{y}" width="216" height="116" rx="16" fill="#12141a" stroke="#f97316" stroke-opacity=".3" stroke-width="1.5"/>
<circle cx="{x + 196}" cy="{y + 20}" r="4" fill="#f97316"><animate attributeName="opacity" values="1;.2;1" dur="{1.6 + i * .3}s" repeatCount="indefinite"/></circle>
<text x="{x + 22}" y="{y + 66}" class="sans" font-size="46" font-weight="900" fill="url(#og)">{esc(str(val))}</text>
<text x="{x + 22}" y="{y + 94}" class="mono" font-size="12" fill="#a8a29e" letter-spacing="2.5">{lab}</text>
</g>'''
    shades = ["#fbbf24", "#f97316", "#ea580c", "#fb923c", "#c2410c", "#fdba74"]
    langs = ""
    if d["langs"]:
        for i, (name, pct) in enumerate(d["langs"]):
            y = 92 + i * 32
            bw = max(4, pct / 100 * 250)
            langs += f'''<text x="520" y="{y + 5}" class="mono" font-size="14" fill="#fed7aa">{esc(name)}</text>
<rect x="650" y="{y - 6}" width="250" height="10" rx="5" fill="#f97316" fill-opacity=".12"/>
<rect x="650" y="{y - 6}" width="0" height="10" rx="5" fill="{shades[i % 6]}"><animate attributeName="width" from="0" to="{bw:.1f}" dur="1.2s" begin="{i * .15}s" fill="freeze"/></rect>
<text x="976" y="{y + 5}" text-anchor="end" class="mono" font-size="13" fill="#a8a29e">{pct:.1f}%</text>
'''
    else:
        langs = '<text x="520" y="120" class="mono" font-size="14" fill="#a8a29e">Languages load after the first workflow run.</text>'
    today = datetime.date.today().isoformat()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 300" width="1000" height="300" role="img" aria-label="GitHub stats and top languages for {USER}">
<defs>
<linearGradient id="og" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbbf24"/><stop offset="1" stop-color="#ea580c"/></linearGradient>
<style>.mono{{font-family:{MONO}}}.sans{{font-family:{SANS}}}</style>
</defs>
<rect x="1" y="1" width="998" height="298" rx="20" fill="#0a0a0f" stroke="#f97316" stroke-opacity=".35" stroke-width="2"/>
{t}
<line x1="496" y1="28" x2="496" y2="272" stroke="#f97316" stroke-opacity=".2"/>
<text x="520" y="52" class="mono" font-size="13" fill="#f97316" letter-spacing="3">// TOP LANGUAGES</text>
{langs}
<text x="976" y="288" text-anchor="end" class="mono" font-size="11" fill="#57534e">updated {today}</text>
</svg>'''


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(collect()))
    print("wrote", OUT)
