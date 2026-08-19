<a id="top"></a>

<!-- ========================== HERO ========================== -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:6366f1,100:9333ea&height=220&section=header&text=Amaanullah%20(AK)&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Full-Stack%20Developer%20%7C%20Laravel%20%26%20Flutter%20Specialist&descAlignY=55&descSize=18&animation=fadeIn" width="100%" alt="header banner" />

<img
  src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=22&duration=3000&pause=1000&color=6366F1&center=true&vCenter=true&width=900&lines=Building+production+SaaS+%26+CRM+systems;Real-time+apps+with+PHP%2C+WebSockets+%26+MySQL;Flutter+%2B+Firebase+mobile+experiences;Turning+client+ideas+into+shipped+products;Currently+scaling+a+real-time+chat+platform"
  alt="Animated intro lines"
/>

<br/>

<a href="https://amaanullah.com"><img alt="Portfolio website" src="https://img.shields.io/badge/Portfolio-amaanullah.com-0ea5e9?style=for-the-badge&logo=firefox-browser&logoColor=white"></a>
<a href="https://linkedin.com/in/akamaanullah"><img alt="LinkedIn profile" src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://github.com/akamaanullah"><img alt="GitHub follow" src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"></a>
<a href="https://instagram.com/akamaanullah"><img alt="Instagram profile" src="https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>
<a href="https://behance.net/muhammadzain121"><img alt="Behance portfolio" src="https://img.shields.io/badge/Behance-Portfolio-1769FF?style=for-the-badge&logo=behance&logoColor=white"></a>
<a href="https://linktr.ee/akamaanullah"><img alt="Linktree links" src="https://img.shields.io/badge/Linktree-Links-43E55E?style=for-the-badge&logo=linktree&logoColor=white"></a>

<br/><br/>

<img src="https://komarev.com/ghpvc/?username=akamaanullah&style=for-the-badge&color=6366f1&label=PROFILE+VIEWS" alt="profile views" />

</div>

<br/>

<!-- ========================== NAV ========================== -->
<p align="center">
  <a href="#about"><img src="https://img.shields.io/badge/About%20Me-0ea5e9?style=for-the-badge" /></a>
  <a href="#now"><img src="https://img.shields.io/badge/Currently%20Building-14b8a6?style=for-the-badge" /></a>
  <a href="#services"><img src="https://img.shields.io/badge/Services-22c55e?style=for-the-badge" /></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Skills-f59e0b?style=for-the-badge" /></a>
  <a href="#projects"><img src="https://img.shields.io/badge/Projects-ef4444?style=for-the-badge" /></a>
  <a href="#approach"><img src="https://img.shields.io/badge/How%20I%20Work-8b5cf6?style=for-the-badge" /></a>
  <a href="#stats"><img src="https://img.shields.io/badge/GitHub%20Stats-0ea5e9?style=for-the-badge" /></a>
  <a href="#connect"><img src="https://img.shields.io/badge/Connect-9333ea?style=for-the-badge" /></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:0ea5e9,100:9333ea&height=3&section=footer" width="100%" alt="" />

<!-- ========================== ABOUT ========================== -->
<a id="about"></a>
### <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"/> About Me

I'm a full-stack developer based in Karachi, Pakistan, working under the **AmaanUllah** brand ([amaanullah.com](https://amaanullah.com)) — building custom software for clients across Pakistan, the US, UK, and UAE.

My core focus is **Laravel/PHP backends paired with real-time systems** — CRMs, chat platforms, and SaaS products that need to handle live data, not just CRUD screens. On the mobile side I build with **Flutter + Firebase**, and I round things out with SEO/technical audits so the products I build can actually be found.

I don't just hand off code and disappear — I stay close to production. That means running security audits on my own platforms, fixing database schema issues under load, and treating things like WebSocket scaling, backups, and HTTPS as first-class concerns, not afterthoughts.

**What I'm currently deepening:** React.js and Node.js, to round out a JS-heavy frontend stack alongside my PHP/Flutter backend work.

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== NOW ========================== -->
<a id="now"></a>
### 📅 Currently Building

I'm in an active build-and-harden cycle on **ChatRox**, my own real-time messaging platform — this is the project getting most of my attention right now:

- 🔧 **Multi-tenant architecture upgrade** — migrating the database from a legacy `company_id` schema to a proper `workspace_id` model
- 🔐 **Security hardening** — closing out a full audit that flagged XSS, CSRF, and WebSocket token exposure issues before they hit production
- 📞 **Calling features** — shipped screen sharing for 1-on-1 and group calls (with pin/unpin view), plus per-contact nicknames and granular notification controls (global / DM / channel / mentions)
- ⚙️ **Scalability work** — moving the Ratchet WebSocket server off a single-process setup toward proper horizontal scaling with Redis pub/sub and a process supervisor

Alongside that, I'm learning **React Query, Next.js (RSC), and the Bun runtime**, and exploring ETL/reporting pipelines for product analytics dashboards.

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== SERVICES ========================== -->
<a id="services"></a>
### 🔍 Services

**Custom Laravel Applications**
End-to-end backend builds — role-based access control, multi-tenant architecture, queue-driven background jobs, and transactional email systems. I design schemas that hold up once real users and real data volume show up, not just in a demo.

**Real-Time Systems**
WebSocket-based chat, presence, and notification systems (built on Ratchet), plus the harder problems that come with them: connection scaling, message delivery guarantees, and keeping a single-process server from becoming a bottleneck.

**Flutter + Firebase Mobile Apps**
Auth flows, Firestore/Realtime Database, push notifications via FCM, and media upload pipelines — shipped as production Android/iOS apps, not prototypes.

**Dashboards & Data Visualization**
Admin panels with real reporting behind them — charts, CSV/Excel exports, and audit logs that let a non-technical business owner actually see what's happening in their system.

**UX Design Systems**
Figma component libraries built to hand off cleanly to development, so design and engineering aren't fighting each other mid-sprint.

**Performance & SEO**
Database indexing, query and API optimization, plus technical/on-page SEO audits — including structured data (JSON-LD), redirect cleanup after migrations, and content rewrites grounded in actual Search Console data rather than guesswork.

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== SKILLS ========================== -->
<a id="skills"></a>
### 🧰 Skills

<p align="center">
  <img src="https://skillicons.dev/icons?i=php,laravel,mysql,html,css,js,jquery,react,nodejs,flutter,dart,firebase,git,github,figma,ps,vscode,bootstrap,linux&theme=dark" alt="skills icon set" />
</p>

<table>
<tr>
<td width="50%" valign="top">

**Backend & Data**
- PHP / Laravel (RBAC, multi-tenancy, queues)
- MySQL (schema design, indexing, migrations at scale)
- REST API design
- Ratchet WebSockets (real-time messaging, presence)

</td>
<td width="50%" valign="top">

**Mobile & Frontend**
- Flutter / Dart
- Firebase (Auth, Firestore, Realtime DB, FCM)
- JavaScript / jQuery / React (in progress)
- Node.js (in progress)

</td>
</tr>
<tr>
<td width="50%" valign="top">

**Design & Workflow**
- Figma (component libraries, dev handoff)
- Photoshop
- Bootstrap
- Git / GitHub / CI-CD

</td>
<td width="50%" valign="top">

**AI-Assisted Development**
- Claude Code & Google Antigravity for direct project edits and audits
- Gemini / AI Studio for spec-driven app generation
- Structured unit-testing workflows (happy path + edge cases)

</td>
</tr>
</table>

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== PROJECTS ========================== -->
<a id="projects"></a>
### 🚀 Featured Projects
<sub>(also pinned on my profile)</sub>

<table>
  <tr>
    <th align="left">Project</th>
    <th align="left">What it is</th>
    <th align="left">Stack</th>
    <th align="left">Link</th>
  </tr>
  <tr>
    <td><strong>ChatRox</strong><br/><sub>Real-time chat & collaboration platform</sub></td>
    <td>Custom PHP MVC messaging platform in the style of Slack/Teams — group channels, DMs, screen sharing on calls, presence, mentions, and per-contact controls. Built on Ratchet WebSockets, currently being upgraded to multi-tenant.</td>
    <td><img src="https://skillicons.dev/icons?i=php,laravel,js" height="20" /></td>
    <td><a href="https://amaanullah.com/portfolio-details.php?slug=chatrox--real-time-chat--collaboration-web-app"><img src="https://img.shields.io/badge/Case%20Study-0ea5e9?style=for-the-badge"/></a></td>
  </tr>
  <tr>
    <td><strong>Chatrox Mobile App</strong><br/><sub>Realtime chat on the go</sub></td>
    <td>Flutter companion app for ChatRox — groups, media sharing, push notifications, and live typing/presence indicators, talking to the same WebSocket backend as the web app.</td>
    <td><img src="https://skillicons.dev/icons?i=flutter,dart,firebase" height="20" /></td>
    <td><a href="https://amaanullah.com/portfolio-details.php?slug=chatrox-mobile-app--real-time-communication-on-the-go"><img src="https://img.shields.io/badge/Case%20Study-0ea5e9?style=for-the-badge"/></a></td>
  </tr>
  <tr>
    <td><strong>CRM – Velspra</strong><br/><sub>Sales & leads management system</sub></td>
    <td>Multi-tenant CRM handling 1.5M+ leads and 300+ concurrent users in production — role-based dashboards, exports, activity logs, and performance insights for sales teams.</td>
    <td><img src="https://skillicons.dev/icons?i=laravel,mysql,bootstrap" height="20" /></td>
    <td><a href="https://amaanullah.com/portfolio-details.php?slug=crm-velspra--sales--leads-management-system"><img src="https://img.shields.io/badge/Case%20Study-0ea5e9?style=for-the-badge"/></a></td>
  </tr>
  <tr>
    <td><strong>Tour Guide Mobile App</strong><br/><sub>City explorer with guides, maps & reviews</sub></td>
    <td>Explore Pakistan through curated destinations, interactive maps, and user-submitted reviews — built as a full Flutter + Firebase experience.</td>
    <td><img src="https://skillicons.dev/icons?i=flutter,firebase" height="20" /></td>
    <td><a href="https://amaanullah.com/portfolio-details.php?slug=tour-guide-mobile-app--explore-pakistan-like-never-before"><img src="https://img.shields.io/badge/Case%20Study-0ea5e9?style=for-the-badge"/></a></td>
  </tr>
  <tr>
    <td><strong>Umrah Al Badal</strong><br/><sub>Umrah booking & management platform</sub></td>
    <td>End-to-end service workflow for Umrah bookings — order management, payments, and full admin control over service fulfillment.</td>
    <td><img src="https://skillicons.dev/icons?i=php,laravel,mysql" height="20" /></td>
    <td><a href="https://amaanullah.com/portfolio-details.php?slug=umrah-al-badal--umrah-service-platform"><img src="https://img.shields.io/badge/Case%20Study-0ea5e9?style=for-the-badge"/></a></td>
  </tr>
</table>

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== HOW I WORK ========================== -->
<a id="approach"></a>
### 🧭 How I Work

**I treat my own products like client production systems.** ChatRox isn't a side demo — it's gone through real database migrations under load (72 users, 17,800+ messages moved without data loss), a full security audit, and ongoing scalability work. I hold my own code to the same bar I'd hold a client's.

**I use AI tools deliberately, not as a shortcut around understanding.** Claude Code and Google Antigravity help me move faster on audits and repetitive edits, but every schema change, security fix, and architecture decision gets reviewed against what the system actually needs.

**I close the loop on SEO/growth work with data, not guesses.** When I rewrite a page's title or meta description, it's based on actual Search Console impressions and position data — not just trimming characters to fit a limit.

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== STATS ========================== -->
<a id="stats"></a>
### 📊 GitHub Stats

<div align="center">
<img src="https://github-readme-stats.vercel.app/api?username=akamaanullah&show_icons=true&theme=tokyonight&hide_border=true&bg_color=00000000" alt="GitHub stats" height="165"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=akamaanullah&layout=compact&theme=tokyonight&hide_border=true&bg_color=00000000" alt="Top languages" height="165"/>
<br/>
<img src="https://streak-stats.demolab.com?user=akamaanullah&theme=tokyonight&hide_border=true&background=00000000" alt="GitHub streak" />
<br/>
<img src="https://github-profile-trophy.vercel.app/?username=akamaanullah&theme=tokyonight&no-bg=true&margin-w=8&row=1" alt="trophies" />
</div>

<!-- Contribution snake — animated, requires a GitHub Action in this repo to generate -->
<div align="center">
<img src="https://raw.githubusercontent.com/akamaanullah/akamaanullah/output/github-contribution-grid-snake-dark.svg" alt="contribution snake animation" width="100%"/>
</div>

<p align="right"><a href="#top"><img src="https://img.shields.io/badge/⬆%20Top-0ea5e9?style=flat-square" /></a></p>

---

<!-- ========================== CONNECT ========================== -->
<a id="connect"></a>
### 🤝 Let's Connect

I'm open to freelance/contract work on Laravel backends, real-time systems, and Flutter apps — and to collaborations on technical writing around clean architecture and product analytics.

<p align="center">
<a href="https://amaanullah.com"><img src="https://img.shields.io/badge/Portfolio-Visit-0ea5e9?style=for-the-badge&logo=firefox-browser&logoColor=white"/></a>
<a href="https://linkedin.com/in/akamaanullah"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://github.com/akamaanullah"><img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white"/></a>
<a href="https://instagram.com/akamaanullah"><img src="https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://behance.net/muhammadzain121"><img src="https://img.shields.io/badge/Behance-Portfolio-1769FF?style=for-the-badge&logo=behance&logoColor=white"/></a>
<a href="https://linktr.ee/akamaanullah"><img src="https://img.shields.io/badge/Linktree-Links-43E55E?style=for-the-badge&logo=linktree&logoColor=white"/></a>
</p>

📧 **Collaborations:** [info@amaanullah.com](mailto:info@amaanullah.com)

<p align="center"><i>"Continuous improvement is better than delayed perfection."</i></p>

<details>
<summary><strong>🗓️ Timeline</strong></summary>
<br/>

- **2023** — Started freelancing with Laravel & Flutter
- **2024** — Built e-commerce platforms & admin dashboards for clients
- **2025** — Transitioned into product design & mentoring flows
- **2026** — Building ChatRox as a full production platform: real-time calling, multi-tenancy, and a security-first rebuild

</details>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0ea5e9,50:6366f1,100:9333ea&height=120&section=footer" width="100%" alt="footer" />

<!-- ========================== SEO Helper ==========================
Amaanullah AK full-stack developer Pakistan, Laravel developer Pakistan, Flutter Firebase apps,
real-time chat platform, WebSocket messaging, CRM dashboards, MySQL optimization, REST APIs,
eCommerce Laravel, UI/UX design, Karachi software developer.
=============================================================================== -->
