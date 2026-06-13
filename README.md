<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Veerababu Narni | Multi-Cloud DevOps Architect</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Fraunces:opsz,wght@9..144,300;9..144,700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #060b14;
    --bg2: #0b1220;
    --bg3: #0f1828;
    --surface: #111c2e;
    --surface2: #172035;
    --border: #1e2f48;
    --border-glow: #2a4a7f;
    --accent: #3b82f6;
    --accent2: #06b6d4;
    --accent3: #8b5cf6;
    --gold: #f59e0b;
    --green: #10b981;
    --red: #ef4444;
    --text: #e2e8f0;
    --text2: #94a3b8;
    --text3: #64748b;
    --glow: rgba(59,130,246,0.15);
    --glow2: rgba(6,182,212,0.1);
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    overflow-x: hidden;
  }

  /* ── Grid noise texture overlay ── */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%231e2f48' fill-opacity='0.25'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    pointer-events: none;
    z-index: 0;
    opacity: 0.3;
  }

  .container {
    max-width: 940px;
    margin: 0 auto;
    padding: 0 24px;
    position: relative;
    z-index: 1;
  }

  /* ── Animated gradient top bar ── */
  .topbar {
    height: 3px;
    background: linear-gradient(90deg, var(--accent3), var(--accent), var(--accent2), var(--accent3));
    background-size: 300% 100%;
    animation: slideGradient 4s linear infinite;
  }

  @keyframes slideGradient {
    0% { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
  }

  /* ── Hero ── */
  .hero {
    padding: 72px 0 56px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 48px;
    align-items: center;
  }

  .hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent2);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .hero-eyebrow::before {
    content: '';
    display: inline-block;
    width: 24px;
    height: 1px;
    background: var(--accent2);
  }

  .hero-name {
    font-family: 'Fraunces', serif;
    font-size: clamp(38px, 6vw, 58px);
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -0.02em;
    color: #fff;
    margin-bottom: 8px;
  }

  .hero-name span {
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-title {
    font-size: 17px;
    font-weight: 500;
    color: var(--text2);
    margin-bottom: 24px;
    letter-spacing: 0.01em;
  }

  .hero-quote {
    font-family: 'Fraunces', serif;
    font-size: 16px;
    font-style: italic;
    font-weight: 300;
    color: var(--text2);
    border-left: 2px solid var(--accent);
    padding-left: 16px;
    margin-bottom: 32px;
    line-height: 1.5;
  }

  .hero-links {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 14px;
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text2);
    text-decoration: none;
    background: var(--surface);
    transition: all 0.2s;
    letter-spacing: 0.02em;
  }

  .badge:hover {
    border-color: var(--accent);
    color: var(--text);
    background: var(--surface2);
    transform: translateY(-1px);
    box-shadow: 0 4px 16px var(--glow);
  }

  .badge .dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }

  .dot-blue { background: var(--accent); }
  .dot-cyan { background: var(--accent2); }
  .dot-purple { background: var(--accent3); }
  .dot-red { background: #e74c3c; }

  .hero-avatar {
    position: relative;
  }

  .avatar-ring {
    width: 170px;
    height: 170px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), var(--accent2), var(--accent3));
    padding: 3px;
    animation: rotateBorder 6s linear infinite;
    box-shadow: 0 0 40px var(--glow), 0 0 80px var(--glow2);
  }

  @keyframes rotateBorder {
    0% { filter: hue-rotate(0deg); }
    100% { filter: hue-rotate(360deg); }
  }

  .avatar-inner {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: var(--bg2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 64px;
    overflow: hidden;
  }

  .avatar-inner img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
  }

  /* ── Stats strip ── */
  .stats-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 1px;
    background: var(--border);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 64px;
  }

  .stat-item {
    background: var(--surface);
    padding: 24px 16px;
    text-align: center;
    transition: background 0.2s;
  }

  .stat-item:hover { background: var(--surface2); }

  .stat-value {
    font-family: 'Fraunces', serif;
    font-size: 30px;
    font-weight: 700;
    color: #fff;
    line-height: 1;
    margin-bottom: 6px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .stat-label {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text3);
    font-family: 'JetBrains Mono', monospace;
  }

  /* ── Section ── */
  .section { margin-bottom: 72px; }

  .section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 32px;
  }

  .section-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.2);
    padding: 4px 10px;
    border-radius: 4px;
  }

  .section-title {
    font-family: 'Fraunces', serif;
    font-size: 26px;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.01em;
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ── About ── */
  .about-text {
    font-size: 15px;
    color: var(--text2);
    line-height: 1.8;
    max-width: 720px;
  }

  .about-text strong { color: var(--text); font-weight: 600; }

  /* ── Engagements ── */
  .engagement-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  .engagement-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px;
    display: flex;
    gap: 14px;
    align-items: flex-start;
    transition: all 0.2s;
  }

  .engagement-card:hover {
    border-color: var(--border-glow);
    background: var(--surface2);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px var(--glow);
  }

  .eng-icon {
    font-size: 20px;
    line-height: 1;
    margin-top: 2px;
  }

  .eng-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--accent2);
    margin-bottom: 4px;
  }

  .eng-text {
    font-size: 13.5px;
    color: var(--text2);
    line-height: 1.5;
  }

  /* ── Tech stack ── */
  .stack-group { margin-bottom: 28px; }

  .stack-group-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--text3);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .stack-group-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  .tech-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .tech-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 6px;
    font-size: 12.5px;
    color: var(--text2);
    font-family: 'JetBrains Mono', monospace;
    transition: all 0.2s;
  }

  .tech-pill:hover {
    border-color: var(--accent);
    color: var(--text);
    background: var(--surface2);
    box-shadow: 0 2px 12px var(--glow);
  }

  /* ── Specialisations ── */
  .spec-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }

  .spec-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 20px;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }

  .spec-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(180deg, var(--accent), var(--accent2));
    opacity: 0;
    transition: opacity 0.2s;
  }

  .spec-card:hover {
    border-color: var(--border-glow);
    background: var(--surface2);
    transform: translateY(-2px);
    box-shadow: 0 6px 24px var(--glow);
  }

  .spec-card:hover::before { opacity: 1; }

  .spec-icon { font-size: 22px; margin-bottom: 10px; }

  .spec-title {
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 5px;
  }

  .spec-desc {
    font-size: 12.5px;
    color: var(--text3);
    line-height: 1.55;
  }

  /* ── Certifications ── */
  .cert-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
  }

  .cert-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px 16px;
    text-align: center;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
    text-decoration: none;
    display: block;
  }

  .cert-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, var(--glow), var(--glow2));
    opacity: 0;
    transition: opacity 0.25s;
  }

  .cert-card:hover {
    border-color: var(--accent);
    transform: translateY(-4px);
    box-shadow: 0 12px 40px var(--glow);
  }

  .cert-card:hover::after { opacity: 1; }

  .cert-badge-img {
    width: 80px;
    height: 80px;
    object-fit: contain;
    margin: 0 auto 14px;
    display: block;
    position: relative;
    z-index: 1;
    border-radius: 50%;
    transition: transform 0.25s;
  }

  .cert-card:hover .cert-badge-img { transform: scale(1.08); }

  .cert-name {
    font-size: 12px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.4;
    margin-bottom: 6px;
    position: relative;
    z-index: 1;
  }

  .cert-issuer {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--text3);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    position: relative;
    z-index: 1;
    margin-bottom: 8px;
  }

  .cert-level {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 10px;
    font-family: 'JetBrains Mono', monospace;
    position: relative;
    z-index: 1;
  }

  .level-pro {
    background: rgba(245,158,11,0.1);
    border: 1px solid rgba(245,158,11,0.3);
    color: var(--gold);
  }

  .level-assoc {
    background: rgba(59,130,246,0.1);
    border: 1px solid rgba(59,130,246,0.3);
    color: var(--accent);
  }

  .level-expert {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.3);
    color: var(--accent3);
  }

  /* ── Projects ── */
  .project-list { display: flex; flex-direction: column; gap: 12px; }

  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 22px 24px;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 16px;
    align-items: center;
    text-decoration: none;
    transition: all 0.2s;
  }

  .project-card:hover {
    border-color: var(--border-glow);
    background: var(--surface2);
    transform: translateX(4px);
    box-shadow: -4px 0 20px var(--glow);
  }

  .project-name {
    font-size: 14.5px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 5px;
  }

  .project-stack {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--text3);
    margin-bottom: 8px;
  }

  .project-meta {
    display: flex;
    gap: 12px;
  }

  .meta-pill {
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }

  .meta-green { background: rgba(16,185,129,0.1); color: var(--green); border: 1px solid rgba(16,185,129,0.2); }
  .meta-orange { background: rgba(245,158,11,0.1); color: var(--gold); border: 1px solid rgba(245,158,11,0.2); }
  .meta-blue { background: rgba(59,130,246,0.1); color: var(--accent); border: 1px solid rgba(59,130,246,0.2); }

  .project-stars {
    text-align: right;
  }

  .star-count {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--gold);
  }

  .star-label {
    font-size: 10px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text3);
    text-transform: uppercase;
  }

  /* ── Blog posts ── */
  .post-list { display: flex; flex-direction: column; gap: 8px; }

  .post-link {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 18px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    text-decoration: none;
    color: var(--text2);
    font-size: 13.5px;
    transition: all 0.2s;
  }

  .post-link:hover {
    border-color: var(--accent);
    color: var(--text);
    background: var(--surface2);
    transform: translateX(4px);
  }

  .post-icon {
    font-size: 16px;
    flex-shrink: 0;
  }

  .post-arrow {
    margin-left: auto;
    color: var(--text3);
    font-size: 12px;
    transition: transform 0.2s;
  }

  .post-link:hover .post-arrow { transform: translateX(4px); color: var(--accent); }

  /* ── Goals ── */
  .goals-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }

  .goal-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 18px;
    display: flex;
    gap: 12px;
    align-items: flex-start;
    font-size: 13.5px;
    color: var(--text2);
    transition: all 0.2s;
  }

  .goal-item:hover { border-color: var(--border-glow); background: var(--surface2); }

  .goal-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    font-weight: 700;
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.15);
    width: 28px;
    height: 28px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }

  /* ── Connect ── */
  .connect-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }

  .connect-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 16px;
    text-align: center;
    text-decoration: none;
    transition: all 0.25s;
    display: block;
  }

  .connect-card:hover {
    border-color: var(--border-glow);
    background: var(--surface2);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px var(--glow);
  }

  .connect-icon { font-size: 24px; margin-bottom: 8px; }

  .connect-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--text3);
    margin-bottom: 4px;
  }

  .connect-value {
    font-size: 12px;
    color: var(--text2);
    font-weight: 500;
  }

  /* ── Footer ── */
  .footer {
    border-top: 1px solid var(--border);
    padding: 48px 0 32px;
    text-align: center;
  }

  .footer-quote {
    font-family: 'Fraunces', serif;
    font-size: 20px;
    font-style: italic;
    font-weight: 300;
    color: var(--text2);
    max-width: 600px;
    margin: 0 auto 16px;
    line-height: 1.5;
  }

  .footer-byline {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: var(--text3);
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .footer-bottombar {
    margin-top: 32px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent);
    opacity: 0.4;
  }

  /* ── GitHub stats images ── */
  .github-stats {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
  }

  .stats-img {
    width: 100%;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    display: block;
  }

  /* ── Divider ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--border), transparent);
    margin: 64px 0;
  }

  /* ── Responsive ── */
  @media (max-width: 768px) {
    .hero { grid-template-columns: 1fr; }
    .hero-avatar { display: none; }
    .stats-strip { grid-template-columns: repeat(3, 1fr); }
    .cert-grid { grid-template-columns: repeat(2, 1fr); }
    .connect-grid { grid-template-columns: repeat(2, 1fr); }
    .engagement-grid, .spec-grid, .goals-grid { grid-template-columns: 1fr; }
  }

  /* ── Fade in animation ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section { animation: fadeUp 0.5s ease both; }
</style>
</head>
<body>

<div class="topbar"></div>

<div class="container">

  <!-- ── HERO ── -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-eyebrow">Senior DevOps & Multi-Cloud Architect</div>
      <h1 class="hero-name">Veerababu<br><span>Narni</span></h1>
      <p class="hero-title">Building scalable, resilient & automated cloud infrastructures at scale</p>
      <blockquote class="hero-quote">
        "I don't just teach cloud — I build engineers who ship to production."
      </blockquote>
      <div class="hero-links">
        <a href="http://veera.veeraopstech.online/" class="badge" target="_blank">
          <span class="dot dot-cyan"></span> veeraopstech.online
        </a>
        <a href="https://www.linkedin.com/in/veerababu-narni-b99b05256" class="badge" target="_blank">
          <span class="dot dot-blue"></span> LinkedIn
        </a>
        <a href="https://medium.com/@veerababu.narni232" class="badge" target="_blank">
          <span class="dot dot-purple"></span> Medium Blog
        </a>
        <a href="mailto:veeraopstechnologies@gmail.com" class="badge">
          <span class="dot dot-red"></span> Email
        </a>
      </div>
    </div>
    <div class="hero-avatar">
      <div class="avatar-ring">
        <div class="avatar-inner">
          <img src="veera.jpeg" alt="Veerababu Narni" onerror="this.style.display='none';this.parentElement.innerHTML='👨‍💻'">
        </div>
      </div>
    </div>
  </section>

  <!-- ── STATS ── -->
  <div class="stats-strip">
    <div class="stat-item">
      <div class="stat-value">14+</div>
      <div class="stat-label">Years Experience</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">20K+</div>
      <div class="stat-label">Students Trained</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">3</div>
      <div class="stat-label">Cloud Platforms</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">30+</div>
      <div class="stat-label">Live Projects</div>
    </div>
    <div class="stat-item">
      <div class="stat-value">100%</div>
      <div class="stat-label">Practical</div>
    </div>
  </div>

  <!-- ── ABOUT ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">01 / About</span>
      <h2 class="section-title">Who I Am</h2>
      <div class="section-line"></div>
    </div>
    <p class="about-text">
      I'm a highly accomplished <strong>Senior DevOps & Multi-Cloud Architect</strong> with over <strong>14+ years of real-world industry experience</strong> spanning Amazon Web Services, Microsoft Azure, and Google Cloud Platform. I have personally trained more than <strong>20,000+ engineers</strong>, guiding them from absolute beginner to landing roles at top MNCs and product-based companies across India and abroad.
      <br><br>
      My teaching is rooted in <strong>industry practice</strong> — every concept I deliver is backed by real production experience. I have architected large-scale cloud infrastructures, led DevOps transformations for enterprises, and built CI/CD pipelines powering mission-critical applications. Complex topics like Kubernetes, Terraform, and multi-cloud strategy become second nature under my guidance.
    </p>
  </section>

  <!-- ── ENGAGEMENTS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">02 / Now</span>
      <h2 class="section-title">Current Engagements</h2>
      <div class="section-line"></div>
    </div>
    <div class="engagement-grid">
      <div class="engagement-card">
        <div class="eng-icon">🔭</div>
        <div>
          <div class="eng-label">Working On</div>
          <div class="eng-text">Architecting a multi-cloud disaster recovery solution for a critical enterprise application</div>
        </div>
      </div>
      <div class="engagement-card">
        <div class="eng-icon">🌱</div>
        <div>
          <div class="eng-label">Deep-Diving</div>
          <div class="eng-text">Service mesh technologies (Istio) and advanced FinOps strategies for cloud cost governance</div>
        </div>
      </div>
      <div class="engagement-card">
        <div class="eng-icon">🤝</div>
        <div>
          <div class="eng-label">Open to Collaborate</div>
          <div class="eng-text">Open-source projects in Cloud Security, Serverless Frameworks, and Infrastructure as Code</div>
        </div>
      </div>
      <div class="engagement-card">
        <div class="eng-icon">⚡</div>
        <div>
          <div class="eng-label">Fun Fact</div>
          <div class="eng-text">Once automated an entire dev environment setup with a single script, saving the team hundreds of hours</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ── TECH STACK ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">03 / Stack</span>
      <h2 class="section-title">Technology Arsenal</h2>
      <div class="section-line"></div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">☁️ Cloud Platforms</div>
      <div class="tech-pills">
        <span class="tech-pill">⚡ AWS</span>
        <span class="tech-pill">🔷 Azure</span>
        <span class="tech-pill">🌐 Google Cloud</span>
        <span class="tech-pill">🔴 Oracle Cloud</span>
      </div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">⚙️ DevOps & Orchestration</div>
      <div class="tech-pills">
        <span class="tech-pill">🐳 Docker</span>
        <span class="tech-pill">☸️ Kubernetes</span>
        <span class="tech-pill">🏗️ Terraform</span>
        <span class="tech-pill">🤖 Ansible</span>
        <span class="tech-pill">🔧 Jenkins</span>
        <span class="tech-pill">🐙 ArgoCD</span>
        <span class="tech-pill">⛵ Helm</span>
        <span class="tech-pill">🦊 GitLab CI</span>
        <span class="tech-pill">⚡ GitHub Actions</span>
        <span class="tech-pill">🔓 OpenTofu</span>
      </div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">📊 Observability</div>
      <div class="tech-pills">
        <span class="tech-pill">🔥 Prometheus</span>
        <span class="tech-pill">📈 Grafana</span>
        <span class="tech-pill">🔍 ELK Stack</span>
        <span class="tech-pill">☁️ CloudWatch</span>
      </div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">🤖 AI & ML for DevOps</div>
      <div class="tech-pills">
        <span class="tech-pill">🧠 GitHub Copilot</span>
        <span class="tech-pill">🤖 KubeGPT</span>
        <span class="tech-pill">🔬 AIOps</span>
        <span class="tech-pill">⚡ LLM Pipelines</span>
      </div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">💻 Languages</div>
      <div class="tech-pills">
        <span class="tech-pill">🐍 Python</span>
        <span class="tech-pill">💻 Bash</span>
        <span class="tech-pill">🐹 Go</span>
      </div>
    </div>

    <div class="stack-group">
      <div class="stack-group-title">🗄️ Databases</div>
      <div class="tech-pills">
        <span class="tech-pill">🐘 PostgreSQL</span>
        <span class="tech-pill">🐬 MySQL</span>
        <span class="tech-pill">🍃 MongoDB</span>
      </div>
    </div>
  </section>

  <!-- ── SPECIALISATIONS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">04 / Expertise</span>
      <h2 class="section-title">What I Specialise In</h2>
      <div class="section-line"></div>
    </div>
    <div class="spec-grid">
      <div class="spec-card">
        <div class="spec-icon">🎯</div>
        <div class="spec-title">Project-Based Learning</div>
        <div class="spec-desc">Every module built around real-world deployments — not just slides or theory.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🏭</div>
        <div class="spec-title">Enterprise Cloud Architecture</div>
        <div class="spec-desc">Production-grade infrastructure design on AWS, Azure, and GCP at scale.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">☸️</div>
        <div class="spec-title">Kubernetes & Containers</div>
        <div class="spec-desc">Docker, EKS, AKS, GKE, Helm, ArgoCD — full GitOps workflows end-to-end.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🔧</div>
        <div class="spec-title">Infrastructure as Code</div>
        <div class="spec-desc">Terraform, Ansible, OpenTofu — complete cloud automation from scratch.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🤖</div>
        <div class="spec-title">AI & ML for DevOps</div>
        <div class="spec-desc">KubeGPT, GitHub Copilot, AIOps, and LLM-powered CI/CD pipelines.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🔒</div>
        <div class="spec-title">Cloud Security</div>
        <div class="spec-desc">IAM, SSO, VPC hardening, zero-trust architecture, and compliance frameworks.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">📊</div>
        <div class="spec-title">Observability</div>
        <div class="spec-desc">Prometheus, Grafana, ELK Stack, CloudWatch — full-stack alerting and tracing.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🌍</div>
        <div class="spec-title">Multi-Cloud Strategy</div>
        <div class="spec-desc">Cost optimisation, cloud-native migration, and hybrid governance at enterprise scale.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🚀</div>
        <div class="spec-title">Career Placement</div>
        <div class="spec-desc">Engineers placed at Amazon, Microsoft, TCS, Infosys, Wipro & high-growth startups.</div>
      </div>
      <div class="spec-card">
        <div class="spec-icon">🎓</div>
        <div class="spec-title">Lead Trainer</div>
        <div class="spec-desc">Most sought-after multi-cloud & DevOps instructor with 20,000+ engineers trained.</div>
      </div>
    </div>
  </section>

  <!-- ── CERTIFICATIONS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">05 / Credentials</span>
      <h2 class="section-title">Certifications</h2>
      <div class="section-line"></div>
    </div>
    <div class="cert-grid">

      <!-- AWS Solutions Architect -->
      <a class="cert-card" href="https://www.credly.com/badges/ff07c2a6-a093-44fd-acc7-8534995f2dca" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/2d84e428-9078-49b6-a804-13c15383d0de/image.png"
          alt="AWS Certified Solutions Architect"
          onerror="this.style.display='none'">
        <div class="cert-name">AWS Certified Solutions Architect</div>
        <div class="cert-issuer">Amazon Web Services</div>
        <span class="cert-level level-pro">⭐ Professional</span>
      </a>

      <!-- CKA -->
      <a class="cert-card" href="https://www.credly.com/badges/afe77f2b-843a-413c-925d-4c8ea7891503" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/8b8ed108-e77d-4396-ac59-2504583b9d54/cka_from_cncfsite__281_29.png"
          alt="Certified Kubernetes Administrator"
          onerror="this.style.display='none'">
        <div class="cert-name">Certified Kubernetes Administrator (CKA)</div>
        <div class="cert-issuer">Linux Foundation / CNCF</div>
        <span class="cert-level level-pro">⭐ Professional</span>
      </a>

      <!-- Azure DevOps -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/c3ab66f8-5d59-4afa-a6c2-0ba30a1989ca/CERT-Expert-DevOps-Engineer-600x600.png"
          alt="Azure DevOps Engineer Expert"
          onerror="this.style.background='#1e2d44';this.style.borderRadius='50%';this.innerHTML='🔷'">
        <div class="cert-name">Microsoft Azure DevOps Engineer</div>
        <div class="cert-issuer">Microsoft Azure</div>
        <span class="cert-level level-expert">⭐ Expert</span>
      </a>

      <!-- Terraform -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/99289602-861e-4929-8277-773e63a2fa6f/image.png"
          alt="HashiCorp Terraform Associate"
          onerror="this.style.display='none'">
        <div class="cert-name">HashiCorp Terraform Associate</div>
        <div class="cert-issuer">HashiCorp</div>
        <span class="cert-level level-assoc">✅ Associate</span>
      </a>

      <!-- GCP -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/fba6f3b1-0190-4715-9c26-0dab49b87d55/image.png"
          alt="Google Cloud DevOps Engineer"
          onerror="this.style.display='none'">
        <div class="cert-name">Google Cloud Professional DevOps Engineer</div>
        <div class="cert-issuer">Google Cloud</div>
        <span class="cert-level level-pro">⭐ Professional</span>
      </a>

      <!-- Docker -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/b0c5445a-72a2-46ad-6a7a-c43d15d3cd46/image.png"
          alt="Docker Certified Associate"
          onerror="this.style.display='none'">
        <div class="cert-name">Docker Certified Associate (DCA)</div>
        <div class="cert-issuer">Docker Inc.</div>
        <span class="cert-level level-assoc">✅ Associate</span>
      </a>

      <!-- AWS DevOps Engineer - NEW -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/bd31ef42-d460-493e-8503-39592aaf0458/image.png"
          alt="AWS DevOps Engineer Professional"
          onerror="this.style.display='none'">
        <div class="cert-name">AWS Certified DevOps Engineer</div>
        <div class="cert-issuer">Amazon Web Services</div>
        <span class="cert-level level-pro">⭐ Professional</span>
      </a>

      <!-- CKAD - NEW -->
      <a class="cert-card" href="#" target="_blank">
        <img class="cert-badge-img"
          src="https://images.credly.com/size/680x680/images/f88d800c-5261-45c6-9515-0458e31c3e16/ckad_from_cncfsite.png"
          alt="Certified Kubernetes Application Developer"
          onerror="this.style.display='none'">
        <div class="cert-name">Certified Kubernetes Application Developer (CKAD)</div>
        <div class="cert-issuer">Linux Foundation / CNCF</div>
        <span class="cert-level level-pro">⭐ Professional</span>
      </a>

    </div>
  </section>

  <!-- ── PROJECTS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">06 / Work</span>
      <h2 class="section-title">Featured Projects</h2>
      <div class="section-line"></div>
    </div>
    <div class="project-list">
      <a class="project-card" href="https://github.com/CloudTechDevOps/multi-cloud-cicd-pipeline" target="_blank">
        <div>
          <div class="project-name">🌟 Multi-Cloud CI/CD Pipeline</div>
          <div class="project-stack">AWS · Azure DevOps · Jenkins · Docker · Kubernetes · Terraform</div>
          <div class="project-meta">
            <span class="meta-pill meta-green">Production Ready</span>
            <span class="meta-pill meta-blue">70+ Forks</span>
          </div>
        </div>
        <div class="project-stars">
          <div class="star-count">250+</div>
          <div class="star-label">⭐ Stars</div>
        </div>
      </a>
      <a class="project-card" href="https://github.com/CloudTechDevOps/serverless-datalake-aws" target="_blank">
        <div>
          <div class="project-name">🔥 Serverless Data Lake on AWS</div>
          <div class="project-stack">AWS Lambda · S3 · Glue · Athena · Lake Formation · Python</div>
          <div class="project-meta">
            <span class="meta-pill meta-green">Complete & Optimised</span>
            <span class="meta-pill meta-blue">50+ Forks</span>
          </div>
        </div>
        <div class="project-stars">
          <div class="star-count">180+</div>
          <div class="star-label">⭐ Stars</div>
        </div>
      </a>
      <a class="project-card" href="https://github.com/CloudTechDevOps/kubernetes-gitops-argocd" target="_blank">
        <div>
          <div class="project-name">⚡ Kubernetes Cluster with GitOps</div>
          <div class="project-stack">Kubernetes · Argo CD · Helm · Terraform · GitHub Actions</div>
          <div class="project-meta">
            <span class="meta-pill meta-orange">In Development</span>
            <span class="meta-pill meta-blue">30+ Forks</span>
          </div>
        </div>
        <div class="project-stars">
          <div class="star-count">120+</div>
          <div class="star-label">⭐ Stars</div>
        </div>
      </a>
    </div>
  </section>

  <!-- ── GITHUB STATS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">07 / Analytics</span>
      <h2 class="section-title">GitHub Analytics</h2>
      <div class="section-line"></div>
    </div>
    <div class="github-stats">
      <img class="stats-img" src="https://streak-stats.demolab.com?user=CloudTechDevOps&theme=tokyonight&hide_border=true&ring=3b82f6&fire=06b6d4&currStreakLabel=8b5cf6" alt="GitHub Streak" />
      <img class="stats-img" src="https://github-readme-activity-graph.vercel.app/graph?username=CloudTechDevOps&theme=tokyo-night&bg_color=0b1220&color=3b82f6&line=06b6d4&point=8b5cf6&area=true&hide_border=true" alt="Contribution Graph" />
    </div>
  </section>

  <!-- ── BLOG POSTS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">08 / Writing</span>
      <h2 class="section-title">Latest Articles</h2>
      <div class="section-line"></div>
    </div>
    <div class="post-list">
      <a class="post-link" href="https://medium.com/@veerababu.narni232/how-to-deploy-a-self-hosted-agent-in-azure-pipeline-c07a4f4ca4c4" target="_blank">
        <span class="post-icon">📖</span>
        How to Deploy a Self-Hosted Agent in Azure Pipeline
        <span class="post-arrow">→</span>
      </a>
      <a class="post-link" href="https://medium.com/@veerababu.narni232/querying-data-in-s3-with-amazon-athena-d9319eb87155" target="_blank">
        <span class="post-icon">🔧</span>
        Querying Data in S3 with Amazon Athena
        <span class="post-arrow">→</span>
      </a>
      <a class="post-link" href="https://medium.com/@veerababu.narni232/everything-you-need-to-know-about-aws-eks-auto-mode-b5e03b49b630" target="_blank">
        <span class="post-icon">☁️</span>
        Everything You Need to Know About AWS EKS Auto Mode
        <span class="post-arrow">→</span>
      </a>
      <a class="post-link" href="https://medium.com/@veerababu.narni232/centralizing-secure-cloud-networks-hands-on-guide-to-deploying-aws-transit-gateway-1032221d4263" target="_blank">
        <span class="post-icon">🚀</span>
        Centralising Cloud Networks: A Practical Guide to Deploying AWS Transit Gateway
        <span class="post-arrow">→</span>
      </a>
    </div>
  </section>

  <!-- ── GOALS ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">09 / 2026</span>
      <h2 class="section-title">Goals This Year</h2>
      <div class="section-line"></div>
    </div>
    <div class="goals-grid">
      <div class="goal-item">
        <div class="goal-num">01</div>
        Contribute to 5+ significant open-source DevOps tools and maintain widely-used Terraform modules
      </div>
      <div class="goal-item">
        <div class="goal-num">02</div>
        Achieve AWS Certified DevOps Engineer – Professional certification
      </div>
      <div class="goal-item">
        <div class="goal-num">03</div>
        Mentor aspiring cloud engineers and grow the community of practitioners
      </div>
      <div class="goal-item">
        <div class="goal-num">04</div>
        Publish 6+ in-depth technical articles covering multi-cloud architecture and FinOps
      </div>
    </div>
  </section>

  <!-- ── CONNECT ── -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">10 / Connect</span>
      <h2 class="section-title">Let's Build Together</h2>
      <div class="section-line"></div>
    </div>
    <div class="connect-grid">
      <a class="connect-card" href="https://www.linkedin.com/in/veerababu-narni-b99b05256" target="_blank">
        <div class="connect-icon">💼</div>
        <div class="connect-label">LinkedIn</div>
        <div class="connect-value">veerababu-narni</div>
      </a>
      <a class="connect-card" href="http://veera.veeraopstech.online/" target="_blank">
        <div class="connect-icon">🌐</div>
        <div class="connect-label">Website</div>
        <div class="connect-value">veeraopstech.online</div>
      </a>
      <a class="connect-card" href="https://medium.com/@veerababu.narni232" target="_blank">
        <div class="connect-icon">✍️</div>
        <div class="connect-label">Medium</div>
        <div class="connect-value">@veerababu.narni232</div>
      </a>
      <a class="connect-card" href="mailto:veeraopstechnologies@gmail.com">
        <div class="connect-icon">📧</div>
        <div class="connect-label">Email</div>
        <div class="connect-value">veeraopstechnologies</div>
      </a>
    </div>
  </section>

</div>

<!-- ── FOOTER ── -->
<div class="container">
  <footer class="footer">
    <p class="footer-quote">
      "The best way to learn Multi-Cloud DevOps is to build real systems — not memorise commands."
    </p>
    <p class="footer-byline">— Veerababu Narni · Senior DevOps & Multi-Cloud Architect</p>
    <div class="footer-bottombar"></div>
  </footer>
</div>

</body>
</html>
