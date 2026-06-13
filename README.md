

<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--font-sans)}
.wrap{padding:0 0 2rem}
.topbar{height:3px;background:linear-gradient(90deg,#6366f1,#3b82f6,#06b6d4,#6366f1);background-size:200% 100%;animation:slide 3s linear infinite}
@keyframes slide{0%{background-position:0%}100%{background-position:200%}}
.hero{display:grid;grid-template-columns:1fr auto;gap:2rem;align-items:center;padding:2rem 1.5rem 1.5rem}
.eyebrow{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--color-text-info);margin-bottom:.5rem;display:flex;align-items:center;gap:8px}
.eyebrow::before{content:'';display:inline-block;width:20px;height:1px;background:currentColor}
.hero-name{font-size:38px;font-weight:500;line-height:1.05;color:var(--color-text-primary);margin-bottom:.3rem}
.hero-name span{color:var(--color-text-info)}
.hero-sub{font-size:14px;color:var(--color-text-secondary);margin-bottom:1rem;line-height:1.5}
.hero-quote{font-family:var(--font-serif);font-size:14px;font-style:italic;color:var(--color-text-secondary);border-left:2px solid var(--color-border-info);padding-left:12px;margin-bottom:1.25rem;line-height:1.55}
.pill-row{display:flex;flex-wrap:wrap;gap:8px}
.pill{display:inline-flex;align-items:center;gap:6px;padding:5px 12px;border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-md);font-size:12px;color:var(--color-text-secondary);background:var(--color-background-secondary);text-decoration:none;cursor:pointer}
.pill:hover{border-color:var(--color-border-info);color:var(--color-text-info)}
.dot{width:6px;height:6px;border-radius:50%;display:inline-block;flex-shrink:0}
.d-blue{background:#3b82f6}.d-cyan{background:#06b6d4}.d-purple{background:#8b5cf6}.d-red{background:#ef4444}
.avatar-wrap{width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#3b82f6,#06b6d4);padding:3px;flex-shrink:0}
.avatar-inner{width:100%;height:100%;border-radius:50%;background:var(--color-background-secondary);display:flex;align-items:center;justify-content:center;font-size:42px;overflow:hidden}
.avatar-inner img{width:100%;height:100%;object-fit:cover;border-radius:50%}
.stats{display:grid;grid-template-columns:repeat(5,1fr);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);overflow:hidden;margin:0 1.5rem 2rem}
.stat{background:var(--color-background-secondary);padding:16px 10px;text-align:center;border-right:0.5px solid var(--color-border-tertiary)}
.stat:last-child{border-right:none}
.stat-v{font-size:22px;font-weight:500;color:var(--color-text-info);line-height:1;margin-bottom:4px}
.stat-l{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-tertiary)}
.sec{padding:0 1.5rem;margin-bottom:2rem}
.sec-hd{display:flex;align-items:center;gap:10px;margin-bottom:1.25rem}
.sec-tag{font-size:10px;letter-spacing:.15em;text-transform:uppercase;color:var(--color-text-info);background:var(--color-background-info);border:0.5px solid var(--color-border-info);padding:3px 10px;border-radius:var(--border-radius-md)}
.sec-title{font-size:18px;font-weight:500;color:var(--color-text-primary)}
.sec-line{flex:1;height:0.5px;background:var(--color-border-tertiary)}
.about-p{font-size:14px;color:var(--color-text-secondary);line-height:1.8}
.about-p strong{color:var(--color-text-primary);font-weight:500}
.eng-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.eng-card{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:14px 16px;display:flex;gap:12px;align-items:flex-start}
.eng-ico{font-size:18px;line-height:1;margin-top:2px;color:var(--color-text-info)}
.eng-lbl{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-tertiary);margin-bottom:3px}
.eng-txt{font-size:13px;color:var(--color-text-secondary);line-height:1.5}
.stack-grp{margin-bottom:1.25rem}
.stack-lbl{font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--color-text-tertiary);margin-bottom:8px;display:flex;align-items:center;gap:8px}
.stack-lbl::after{content:'';flex:1;height:0.5px;background:var(--color-border-tertiary)}
.tech-pills{display:flex;flex-wrap:wrap;gap:7px}
.tech-p{display:inline-flex;align-items:center;padding:5px 11px;background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-md);font-size:12px;color:var(--color-text-secondary)}
.spec-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.spec-card{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:16px 18px;transition:border-color .15s}
.spec-card:hover{border-color:var(--color-border-info)}
.spec-ico{font-size:20px;margin-bottom:8px;color:var(--color-text-info)}
.spec-t{font-size:13px;font-weight:500;color:var(--color-text-primary);margin-bottom:4px}
.spec-d{font-size:12px;color:var(--color-text-tertiary);line-height:1.5}
.cert-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.cert-card{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:20px 12px 16px;text-align:center;text-decoration:none;display:block;transition:border-color .15s}
.cert-card:hover{border-color:var(--color-border-info)}
.cert-img{width:72px;height:72px;object-fit:contain;border-radius:50%;margin:0 auto 12px;display:block}
.cert-fallback{width:72px;height:72px;border-radius:50%;background:var(--color-background-info);display:flex;align-items:center;justify-content:center;margin:0 auto 12px;font-size:28px}
.cert-n{font-size:12px;font-weight:500;color:var(--color-text-primary);line-height:1.4;margin-bottom:5px}
.cert-iss{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--color-text-tertiary);margin-bottom:8px}
.lvl{display:inline-block;padding:3px 10px;border-radius:20px;font-size:10px}
.lv-pro{background:var(--color-background-warning);color:var(--color-text-warning);border:0.5px solid var(--color-border-warning)}
.lv-assoc{background:var(--color-background-info);color:var(--color-text-info);border:0.5px solid var(--color-border-info)}
.lv-exp{background:var(--color-background-primary);color:var(--color-text-secondary);border:0.5px solid var(--color-border-secondary)}
.proj-list{display:flex;flex-direction:column;gap:10px}
.proj-card{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:18px 20px;display:grid;grid-template-columns:1fr auto;gap:12px;align-items:center;text-decoration:none;transition:border-color .15s}
.proj-card:hover{border-color:var(--color-border-info)}
.proj-n{font-size:14px;font-weight:500;color:var(--color-text-primary);margin-bottom:4px}
.proj-st{font-size:11px;color:var(--color-text-tertiary);margin-bottom:8px}
.proj-meta{display:flex;gap:8px}
.mp{font-size:11px;padding:3px 9px;border-radius:var(--border-radius-md)}
.mp-g{background:var(--color-background-success);color:var(--color-text-success);border:0.5px solid var(--color-border-success)}
.mp-a{background:var(--color-background-warning);color:var(--color-text-warning);border:0.5px solid var(--color-border-warning)}
.mp-b{background:var(--color-background-info);color:var(--color-text-info);border:0.5px solid var(--color-border-info)}
.proj-stars{text-align:right}
.star-v{font-size:20px;font-weight:500;color:var(--color-text-warning)}
.star-l{font-size:10px;text-transform:uppercase;letter-spacing:.08em;color:var(--color-text-tertiary)}
.post-list{display:flex;flex-direction:column;gap:8px}
.post-a{display:flex;align-items:center;gap:12px;padding:13px 16px;background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);text-decoration:none;font-size:13px;color:var(--color-text-secondary);transition:border-color .15s}
.post-a:hover{border-color:var(--color-border-info);color:var(--color-text-primary)}
.post-arr{margin-left:auto;font-size:14px;color:var(--color-text-tertiary)}
.post-a:hover .post-arr{color:var(--color-text-info)}
.goals-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.goal-item{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:14px 16px;display:flex;gap:12px;align-items:flex-start;font-size:13px;color:var(--color-text-secondary)}
.g-num{font-size:11px;font-weight:500;color:var(--color-text-info);background:var(--color-background-info);border:0.5px solid var(--color-border-info);width:28px;height:28px;border-radius:var(--border-radius-md);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px}
.conn-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.conn-card{background:var(--color-background-secondary);border:0.5px solid var(--color-border-tertiary);border-radius:var(--border-radius-lg);padding:18px 12px;text-align:center;text-decoration:none;transition:border-color .15s;display:block}
.conn-card:hover{border-color:var(--color-border-info)}
.conn-ico{font-size:22px;color:var(--color-text-info);margin-bottom:8px}
.conn-lbl{font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-tertiary);margin-bottom:3px}
.conn-val{font-size:12px;color:var(--color-text-secondary)}
.footer{border-top:0.5px solid var(--color-border-tertiary);padding:2rem 1.5rem 1rem;text-align:center}
.fq{font-family:var(--font-serif);font-size:16px;font-style:italic;font-weight:400;color:var(--color-text-secondary);max-width:520px;margin:0 auto .75rem;line-height:1.55}
.fb{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-tertiary)}
.divider{height:0.5px;background:var(--color-border-tertiary);margin:0 1.5rem}
</style>

<div class="wrap">
<h2 class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden">Veerababu Narni – Senior DevOps and Multi-Cloud Architect profile</h2>
<div class="topbar"></div>

<!-- Hero -->
<div class="hero">
  <div>
    <div class="eyebrow">Senior DevOps & Multi-Cloud Architect</div>
    <div class="hero-name">Veerababu <span>Narni</span></div>
    <div class="hero-sub">Building scalable, resilient & automated cloud infrastructures at enterprise scale</div>
    <blockquote class="hero-quote">"I don't just teach cloud — I build engineers who ship to production."</blockquote>
    <div class="pill-row">
      <a class="pill" href="http://veera.veeraopstech.online/" target="_blank"><span class="dot d-cyan"></span>veeraopstech.online</a>
      <a class="pill" href="https://www.linkedin.com/in/veerababu-narni-b99b05256" target="_blank"><span class="dot d-blue"></span>LinkedIn</a>
      <a class="pill" href="https://medium.com/@veerababu.narni232" target="_blank"><span class="dot d-purple"></span>Medium</a>
      <a class="pill" href="mailto:veeraopstechnologies@gmail.com"><span class="dot d-red"></span>Email</a>
    </div>
  </div>
  <div class="avatar-wrap">
    <div class="avatar-inner">
      <img src="veera.jpeg" alt="Veerababu Narni" onerror="this.style.display='none';this.parentElement.innerHTML='👨‍💻'">
    </div>
  </div>
</div>

<!-- Stats -->
<div class="stats">
  <div class="stat"><div class="stat-v">14+</div><div class="stat-l">Years exp.</div></div>
  <div class="stat"><div class="stat-v">20K+</div><div class="stat-l">Students</div></div>
  <div class="stat"><div class="stat-v">3</div><div class="stat-l">Cloud platforms</div></div>
  <div class="stat"><div class="stat-v">30+</div><div class="stat-l">Live projects</div></div>
  <div class="stat"><div class="stat-v">100%</div><div class="stat-l">Practical</div></div>
</div>

<!-- About -->
<div class="sec">
  <div class="sec-hd"><span class="sec-tag">01 / about</span><span class="sec-title">Who I am</span><div class="sec-line"></div></div>
  <p class="about-p">I'm a highly accomplished <strong>Senior DevOps & Multi-Cloud Architect</strong> with over <strong>14+ years of real-world industry experience</strong> spanning AWS, Microsoft Azure, and Google Cloud Platform. I have personally trained more than <strong>20,000+ engineers</strong>, guiding them from beginner level to landing roles at top MNCs and product companies across India and abroad. Every concept I deliver is backed by real production experience — large-scale infrastructure, enterprise DevOps transformations, and CI/CD pipelines powering mission-critical applications.</p>
</div>

<div class="divider"></div>

<!-- Engagements -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">02 / now</span><span class="sec-title">Current engagements</span><div class="sec-line"></div></div>
  <div class="eng-grid">
    <div class="eng-card"><i class="ti ti-telescope eng-ico" aria-hidden="true"></i><div><div class="eng-lbl">Working on</div><div class="eng-txt">Multi-cloud disaster recovery solution for a critical enterprise application</div></div></div>
    <div class="eng-card"><i class="ti ti-brand-github eng-ico" aria-hidden="true"></i><div><div class="eng-lbl">Open to collaborate</div><div class="eng-txt">Cloud Security, Serverless Frameworks, and Infrastructure as Code projects</div></div></div>
    <div class="eng-card"><i class="ti ti-topology-star eng-ico" aria-hidden="true"></i><div><div class="eng-lbl">Deep-diving</div><div class="eng-txt">Istio service mesh and advanced FinOps strategies for cost governance</div></div></div>
    <div class="eng-card"><i class="ti ti-bolt eng-ico" aria-hidden="true"></i><div><div class="eng-lbl">Fun fact</div><div class="eng-txt">Once automated an entire dev environment setup in a single script, saving hundreds of hours</div></div></div>
  </div>
</div>

<div class="divider"></div>

<!-- Tech Stack -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">03 / stack</span><span class="sec-title">Technology arsenal</span><div class="sec-line"></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-cloud" style="font-size:13px" aria-hidden="true"></i> Cloud platforms</div><div class="tech-pills"><span class="tech-p">AWS</span><span class="tech-p">Azure</span><span class="tech-p">Google Cloud</span><span class="tech-p">Oracle Cloud</span></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-settings" style="font-size:13px" aria-hidden="true"></i> DevOps & orchestration</div><div class="tech-pills"><span class="tech-p">Docker</span><span class="tech-p">Kubernetes</span><span class="tech-p">Terraform</span><span class="tech-p">Ansible</span><span class="tech-p">Jenkins</span><span class="tech-p">ArgoCD</span><span class="tech-p">Helm</span><span class="tech-p">GitLab CI</span><span class="tech-p">GitHub Actions</span><span class="tech-p">OpenTofu</span></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-chart-line" style="font-size:13px" aria-hidden="true"></i> Observability</div><div class="tech-pills"><span class="tech-p">Prometheus</span><span class="tech-p">Grafana</span><span class="tech-p">ELK Stack</span><span class="tech-p">CloudWatch</span></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-robot" style="font-size:13px" aria-hidden="true"></i> AI & ML for DevOps</div><div class="tech-pills"><span class="tech-p">GitHub Copilot</span><span class="tech-p">KubeGPT</span><span class="tech-p">AIOps</span><span class="tech-p">LLM Pipelines</span></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-code" style="font-size:13px" aria-hidden="true"></i> Languages</div><div class="tech-pills"><span class="tech-p">Python</span><span class="tech-p">Bash</span><span class="tech-p">Go</span></div></div>
  <div class="stack-grp"><div class="stack-lbl"><i class="ti ti-database" style="font-size:13px" aria-hidden="true"></i> Databases</div><div class="tech-pills"><span class="tech-p">PostgreSQL</span><span class="tech-p">MySQL</span><span class="tech-p">MongoDB</span></div></div>
</div>

<div class="divider"></div>

<!-- Specialisations -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">04 / expertise</span><span class="sec-title">What I specialise in</span><div class="sec-line"></div></div>
  <div class="spec-grid">
    <div class="spec-card"><i class="ti ti-target spec-ico" aria-hidden="true"></i><div class="spec-t">Project-based learning</div><div class="spec-d">Every module built around real-world deployments — not just slides.</div></div>
    <div class="spec-card"><i class="ti ti-building-skyscraper spec-ico" aria-hidden="true"></i><div class="spec-t">Enterprise cloud architecture</div><div class="spec-d">Production-grade infra design on AWS, Azure, and GCP at scale.</div></div>
    <div class="spec-card"><i class="ti ti-pentagon spec-ico" aria-hidden="true"></i><div class="spec-t">Kubernetes & containers</div><div class="spec-d">Docker, EKS, AKS, GKE, Helm, ArgoCD — full GitOps workflows.</div></div>
    <div class="spec-card"><i class="ti ti-code-circle spec-ico" aria-hidden="true"></i><div class="spec-t">Infrastructure as Code</div><div class="spec-d">Terraform, Ansible, OpenTofu — complete cloud automation from scratch.</div></div>
    <div class="spec-card"><i class="ti ti-robot spec-ico" aria-hidden="true"></i><div class="spec-t">AI & ML for DevOps</div><div class="spec-d">KubeGPT, Copilot, AIOps and LLM-powered CI/CD pipelines.</div></div>
    <div class="spec-card"><i class="ti ti-shield-lock spec-ico" aria-hidden="true"></i><div class="spec-t">Cloud security</div><div class="spec-d">IAM, SSO, VPC hardening, zero-trust and compliance architecture.</div></div>
    <div class="spec-card"><i class="ti ti-activity spec-ico" aria-hidden="true"></i><div class="spec-t">Observability</div><div class="spec-d">Prometheus, Grafana, ELK Stack — full-stack alerting and tracing.</div></div>
    <div class="spec-card"><i class="ti ti-world spec-ico" aria-hidden="true"></i><div class="spec-t">Multi-cloud strategy</div><div class="spec-d">Cost optimisation, cloud-native migration and hybrid governance.</div></div>
    <div class="spec-card"><i class="ti ti-rocket spec-ico" aria-hidden="true"></i><div class="spec-t">Career placement</div><div class="spec-d">Engineers placed at Amazon, Microsoft, TCS, Infosys, Wipro & startups.</div></div>
    <div class="spec-card"><i class="ti ti-school spec-ico" aria-hidden="true"></i><div class="spec-t">Lead trainer</div><div class="spec-d">Most sought-after multi-cloud & DevOps instructor, 20,000+ trained.</div></div>
  </div>
</div>

<div class="divider"></div>

<!-- Certifications -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">05 / credentials</span><span class="sec-title">Certifications</span><div class="sec-line"></div></div>
  <div class="cert-grid">
    <a class="cert-card" href="https://www.credly.com/badges/ff07c2a6-a093-44fd-acc7-8534995f2dca" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/2d84e428-9078-49b6-a804-13c15383d0de/image.png" alt="AWS Solutions Architect" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-cloud" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">AWS Certified Solutions Architect</div>
      <div class="cert-iss">Amazon Web Services</div>
      <span class="lvl lv-pro">⭐ Professional</span>
    </a>
    <a class="cert-card" href="https://www.credly.com/badges/afe77f2b-843a-413c-925d-4c8ea7891503" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/8b8ed108-e77d-4396-ac59-2504583b9d54/cka_from_cncfsite__281_29.png" alt="CKA" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-pentagon" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">Certified Kubernetes Administrator (CKA)</div>
      <div class="cert-iss">Linux Foundation / CNCF</div>
      <span class="lvl lv-pro">⭐ Professional</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/c3ab66f8-5d59-4afa-a6c2-0ba30a1989ca/CERT-Expert-DevOps-Engineer-600x600.png" alt="Azure DevOps" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-brand-azure" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">Microsoft Azure DevOps Engineer</div>
      <div class="cert-iss">Microsoft Azure</div>
      <span class="lvl lv-exp">⭐ Expert</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/99289602-861e-4929-8277-773e63a2fa6f/image.png" alt="Terraform Associate" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-topology-complex" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">HashiCorp Terraform Associate</div>
      <div class="cert-iss">HashiCorp</div>
      <span class="lvl lv-assoc">✅ Associate</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/fba6f3b1-0190-4715-9c26-0dab49b87d55/image.png" alt="GCP DevOps" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-brand-google" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">GCP Professional DevOps Engineer</div>
      <div class="cert-iss">Google Cloud</div>
      <span class="lvl lv-pro">⭐ Professional</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/b0c5445a-72a2-46ad-6a7a-c43d15d3cd46/image.png" alt="Docker DCA" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-brand-docker" style="font-size:28px;color:var(--color-text-info)"></i></div>
      <div class="cert-n">Docker Certified Associate (DCA)</div>
      <div class="cert-iss">Docker Inc.</div>
      <span class="lvl lv-assoc">✅ Associate</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/bd31ef42-d460-493e-8503-39592aaf0458/image.png" alt="AWS DevOps Engineer" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-cloud-computing" style="font-size:28px;color:var(--color-text-warning)"></i></div>
      <div class="cert-n">AWS Certified DevOps Engineer</div>
      <div class="cert-iss">Amazon Web Services</div>
      <span class="lvl lv-pro">⭐ Professional</span>
    </a>
    <a class="cert-card" href="#" target="_blank">
      <img class="cert-img" src="https://images.credly.com/size/680x680/images/f88d800c-5261-45c6-9515-0458e31c3e16/ckad_from_cncfsite.png" alt="CKAD" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
      <div class="cert-fallback" style="display:none"><i class="ti ti-pentagon" style="font-size:28px;color:var(--color-text-warning)"></i></div>
      <div class="cert-n">Certified Kubernetes Application Developer (CKAD)</div>
      <div class="cert-iss">Linux Foundation / CNCF</div>
      <span class="lvl lv-pro">⭐ Professional</span>
    </a>
  </div>
</div>

<div class="divider"></div>

<!-- Projects -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">06 / work</span><span class="sec-title">Featured projects</span><div class="sec-line"></div></div>
  <div class="proj-list">
    <a class="proj-card" href="https://github.com/CloudTechDevOps/multi-cloud-cicd-pipeline" target="_blank">
      <div><div class="proj-n">Multi-Cloud CI/CD Pipeline</div><div class="proj-st">AWS · Azure DevOps · Jenkins · Docker · Kubernetes · Terraform</div><div class="proj-meta"><span class="mp mp-g">Production ready</span><span class="mp mp-b">70+ forks</span></div></div>
      <div class="proj-stars"><div class="star-v">250+</div><div class="star-l">stars</div></div>
    </a>
    <a class="proj-card" href="https://github.com/CloudTechDevOps/serverless-datalake-aws" target="_blank">
      <div><div class="proj-n">Serverless Data Lake on AWS</div><div class="proj-st">AWS Lambda · S3 · Glue · Athena · Lake Formation · Python</div><div class="proj-meta"><span class="mp mp-g">Complete & optimised</span><span class="mp mp-b">50+ forks</span></div></div>
      <div class="proj-stars"><div class="star-v">180+</div><div class="star-l">stars</div></div>
    </a>
    <a class="proj-card" href="https://github.com/CloudTechDevOps/kubernetes-gitops-argocd" target="_blank">
      <div><div class="proj-n">Kubernetes Cluster with GitOps</div><div class="proj-st">Kubernetes · Argo CD · Helm · Terraform · GitHub Actions</div><div class="proj-meta"><span class="mp mp-a">In development</span><span class="mp mp-b">30+ forks</span></div></div>
      <div class="proj-stars"><div class="star-v">120+</div><div class="star-l">stars</div></div>
    </a>
  </div>
</div>

<div class="divider"></div>

<!-- Blog -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">07 / writing</span><span class="sec-title">Latest articles</span><div class="sec-line"></div></div>
  <div class="post-list">
    <a class="post-a" href="https://medium.com/@veerababu.narni232/how-to-deploy-a-self-hosted-agent-in-azure-pipeline-c07a4f4ca4c4" target="_blank"><i class="ti ti-article" style="font-size:16px;color:var(--color-text-info);flex-shrink:0" aria-hidden="true"></i>How to deploy a self-hosted agent in Azure Pipeline<span class="post-arr"><i class="ti ti-arrow-right"></i></span></a>
    <a class="post-a" href="https://medium.com/@veerababu.narni232/querying-data-in-s3-with-amazon-athena-d9319eb87155" target="_blank"><i class="ti ti-article" style="font-size:16px;color:var(--color-text-info);flex-shrink:0" aria-hidden="true"></i>Querying data in S3 with Amazon Athena<span class="post-arr"><i class="ti ti-arrow-right"></i></span></a>
    <a class="post-a" href="https://medium.com/@veerababu.narni232/everything-you-need-to-know-about-aws-eks-auto-mode-b5e03b49b630" target="_blank"><i class="ti ti-article" style="font-size:16px;color:var(--color-text-info);flex-shrink:0" aria-hidden="true"></i>Everything you need to know about AWS EKS Auto Mode<span class="post-arr"><i class="ti ti-arrow-right"></i></span></a>
    <a class="post-a" href="https://medium.com/@veerababu.narni232/centralizing-secure-cloud-networks-hands-on-guide-to-deploying-aws-transit-gateway-1032221d4263" target="_blank"><i class="ti ti-article" style="font-size:16px;color:var(--color-text-info);flex-shrink:0" aria-hidden="true"></i>Centralising cloud networks: deploying AWS Transit Gateway<span class="post-arr"><i class="ti ti-arrow-right"></i></span></a>
  </div>
</div>

<div class="divider"></div>

<!-- Goals -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">08 / 2026</span><span class="sec-title">Goals this year</span><div class="sec-line"></div></div>
  <div class="goals-grid">
    <div class="goal-item"><div class="g-num">01</div>Contribute to 5+ significant open-source DevOps tools and maintain widely-used Terraform modules</div>
    <div class="goal-item"><div class="g-num">02</div>Achieve AWS Certified DevOps Engineer – Professional certification</div>
    <div class="goal-item"><div class="g-num">03</div>Mentor aspiring cloud engineers and grow the practitioner community</div>
    <div class="goal-item"><div class="g-num">04</div>Publish 6+ in-depth technical articles covering multi-cloud architecture and FinOps</div>
  </div>
</div>

<div class="divider"></div>

<!-- Connect -->
<div class="sec" style="margin-top:1.5rem">
  <div class="sec-hd"><span class="sec-tag">09 / connect</span><span class="sec-title">Let's build together</span><div class="sec-line"></div></div>
  <div class="conn-grid">
    <a class="conn-card" href="https://www.linkedin.com/in/veerababu-narni-b99b05256" target="_blank"><i class="ti ti-brand-linkedin conn-ico" aria-hidden="true"></i><div class="conn-lbl">LinkedIn</div><div class="conn-val">veerababu-narni</div></a>
    <a class="conn-card" href="http://veera.veeraopstech.online/" target="_blank"><i class="ti ti-world conn-ico" aria-hidden="true"></i><div class="conn-lbl">Website</div><div class="conn-val">veeraopstech.online</div></a>
    <a class="conn-card" href="https://medium.com/@veerababu.narni232" target="_blank"><i class="ti ti-brand-medium conn-ico" aria-hidden="true"></i><div class="conn-lbl">Medium</div><div class="conn-val">@veerababu.narni232</div></a>
    <a class="conn-card" href="mailto:veeraopstechnologies@gmail.com"><i class="ti ti-mail conn-ico" aria-hidden="true"></i><div class="conn-lbl">Email</div><div class="conn-val">veeraopstechnologies</div></a>
  </div>
</div>

<!-- Footer -->
<div class="footer">
  <p class="fq">"The best way to learn multi-cloud DevOps is to build real systems — not memorise commands."</p>
  <p class="fb">— Veerababu Narni · Senior DevOps & Multi-Cloud Architect</p>
</div>

</div>
