import streamlit as st

st.set_page_config(
    page_title="Saranga Vinod | Marketing Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# EDIT THESE DETAILS BEFORE PUBLISHING
# =========================================================
LINKEDIN_URL = ""  # Add your LinkedIn profile URL
EMAIL_ADDRESS = ""  # Add your professional email
RESUME_URL = ""  # Add a public resume link, if available

GITHUB_PROFILE = "https://github.com/sarangavinod0103-wq"

PROJECTS = [
    {
        "number": "01",
        "title": "WishCare",
        "category": "SOCIAL MEDIA & CONTENT STRATEGY",
        "summary": (
            "A social media and content marketing strategy exploring consumer "
            "research, competitor positioning, campaign development, creator "
            "strategy and community engagement."
        ),
        "contribution": "Marketing strategy · Consumer research",
        "repo": "https://github.com/sarangavinod0103-wq/Wishcare-social-media-strategy",
        "tag": "Brand & Content",
    },
    {
        "number": "02",
        "title": "Lenskart Smart Glasses",
        "category": "BRAND & GO-TO-MARKET STRATEGY",
        "summary": (
            "A strategic marketing project exploring how smart glasses can be "
            "positioned as a natural extension of everyday eyewear through "
            "consumer insight, positioning and go-to-market planning."
        ),
        "contribution": "Consumer insight · Positioning · GTM",
        "repo": "https://github.com/sarangavinod0103-wq/lenskart-smart-glasses-strategy",
        "tag": "Product Marketing",
    },
    {
        "number": "03",
        "title": "VedaCare",
        "category": "BRAND STRATEGY & DIGITAL MARKETING",
        "summary": (
            "A herbal skincare brand strategy covering brand identity, product "
            "portfolio, segmentation, targeting and positioning, and a digital "
            "marketing approach using the POEM framework."
        ),
        "contribution": "Brand strategy · Digital marketing",
        "repo": "https://github.com/sarangavinod0103-wq/vedacare-brand-strategy",
        "tag": "Brand Strategy",
    },
    {
        "number": "04",
        "title": "Amul × Gen Z",
        "category": "CONSUMER-FOCUSED MARKETING",
        "summary": (
            "A Gen Z-focused marketing strategy exploring brand relevance through "
            "product innovation, packaging, influencer engagement, quick commerce "
            "and retail experience."
        ),
        "contribution": "Market analysis · Consumer strategy",
        "repo": "https://github.com/sarangavinod0103-wq/amul-gen-z-marketing-strategy",
        "tag": "Consumer Insights",
    },
]

EXPERIENCES = [
    {
        "company": "Bajaj Capital",
        "role": "Corporate Internship Program — Marketing / Sales",
        "period": "Internship",
        "description": (
            "Customer-facing experience involving mutual fund sales and SIP-related "
            "customer conversations. Add your exact dates and verified target results "
            "before publishing."
        ),
    },
    {
        "company": "Unlimits",
        "role": "Marketing & Design Thinking Intern",
        "period": "Oct–Nov 2025",
        "description": (
            "Conducted 20+ user interviews, developed empathy maps and proposed UI "
            "simplifications to help reduce navigation friction."
        ),
    },
    {
        "company": "Udayan Care",
        "role": "Social Internship Program",
        "period": "Jan 2026",
        "description": (
            "Mentored 15+ children and supported learning and development activities."
        ),
    },
    {
        "company": "Tech Citi Software Consulting",
        "role": "Technical Internship",
        "period": "May 2023",
        "description": "Worked on web pages using HTML and CSS.",
    },
]

# =========================================================
# DESIGN SYSTEM
# =========================================================
st.markdown(
    """
    <style>
    :root {
        --ink: #15243a;
        --muted: #64748b;
        --line: #e2e8f0;
        --paper: #f7f9fc;
        --blue: #315efb;
        --teal: #12a594;
    }

    .stApp {
        background:
            radial-gradient(circle at 88% 3%, rgba(49,94,251,.07), transparent 24rem),
            #f7f9fc;
        color: var(--ink);
    }

    [data-testid="stHeader"] { background: rgba(247,249,252,.92); }
    [data-testid="stSidebar"] { background: #ffffff; }
    .block-container {
        max-width: 1180px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }

    h1, h2, h3 { color: #15243a !important; letter-spacing: -0.035em; }
    p, li { color: #46556b; line-height: 1.72; }
    a { text-decoration: none; }

    .topline {
        display: flex; justify-content: space-between; align-items: center;
        gap: 1rem; padding: .55rem 0 1.1rem 0;
        border-bottom: 1px solid #e2e8f0; margin-bottom: 2.4rem;
    }
    .brand {
        font-weight: 800; color: #15243a; font-size: 1.02rem;
        letter-spacing: -.025em;
    }
    .brand span { color: #315efb; }
    .topnote {
        color: #64748b; font-size: .78rem; letter-spacing: .12em;
        text-transform: uppercase; text-align: right;
    }

    .eyebrow {
        display: inline-block; color: #315efb; font-size: .75rem;
        font-weight: 800; letter-spacing: .16em; text-transform: uppercase;
        margin-bottom: .8rem;
    }
    .hero-title {
        color: #15243a; font-size: clamp(2.8rem, 6vw, 5rem);
        line-height: .99; letter-spacing: -.065em; font-weight: 850;
        margin: .2rem 0 1.25rem 0;
    }
    .hero-title .accent { color: #315efb; }
    .hero-copy {
        color: #526176; font-size: 1.12rem; line-height: 1.8;
        max-width: 720px;
    }
    .hero-panel {
        background: linear-gradient(145deg, #15243a, #233e68);
        border-radius: 24px; padding: 1.8rem; color: white;
        min-height: 260px; display: flex; flex-direction: column;
        justify-content: space-between; box-shadow: 0 18px 50px rgba(21,36,58,.12);
    }
    .hero-panel * { color: white !important; }
    .panel-label { color: #b9c8e3 !important; text-transform: uppercase;
        font-size: .72rem; letter-spacing: .14em; font-weight: 700; }
    .panel-big { font-size: 1.75rem; line-height: 1.2; font-weight: 750;
        letter-spacing: -.04em; margin: 1rem 0; }
    .panel-foot { color: #c8d5e9 !important; font-size: .88rem; }

    .section-kicker {
        color: #315efb; text-transform: uppercase; letter-spacing: .14em;
        font-weight: 800; font-size: .72rem; margin-bottom: .45rem;
    }
    .section-heading {
        font-size: clamp(1.8rem, 3vw, 2.55rem); font-weight: 800;
        letter-spacing: -.05em; color: #15243a; margin: 0 0 .45rem 0;
    }
    .section-intro { color: #64748b; max-width: 720px; margin-bottom: 1.35rem; }

    .project-card {
        height: 100%; background: rgba(255,255,255,.94);
        border: 1px solid #e2e8f0; border-radius: 20px;
        padding: 1.45rem; box-shadow: 0 8px 24px rgba(21,36,58,.035);
    }
    .project-card:hover { border-color: #b7c6ff; }
    .project-number {
        font-size: .75rem; color: #315efb; letter-spacing: .12em;
        font-weight: 800; margin-bottom: 1.1rem;
    }
    .project-tag {
        display: inline-block; border: 1px solid #dbe5ff;
        background: #f2f5ff; color: #3150b7; border-radius: 999px;
        padding: .28rem .65rem; font-size: .72rem; font-weight: 700;
        margin-bottom: .85rem;
    }
    .project-title { font-size: 1.38rem; font-weight: 800; color: #15243a;
        letter-spacing: -.035em; margin-bottom: .35rem; }
    .project-category { color: #64748b; font-size: .69rem; font-weight: 800;
        letter-spacing: .1em; margin-bottom: .85rem; }
    .project-summary { color: #526176; font-size: .93rem; line-height: 1.7; }
    .project-focus { color: #263a58; font-size: .82rem; font-weight: 700;
        border-top: 1px solid #edf0f5; padding-top: .9rem; margin-top: 1rem; }

    .info-card {
        background: #fff; border: 1px solid #e2e8f0; border-radius: 18px;
        padding: 1.25rem 1.35rem; height: 100%;
    }
    .info-label { color: #64748b; font-size: .72rem; text-transform: uppercase;
        letter-spacing: .12em; font-weight: 800; }
    .info-title { color: #15243a; font-size: 1.05rem; font-weight: 800;
        margin: .45rem 0; }
    .info-copy { color: #64748b; font-size: .9rem; line-height: 1.65; }

    .timeline-card {
        border-left: 3px solid #315efb; padding: .15rem 0 .3rem 1.1rem;
        margin: 0 0 1.25rem .2rem;
    }
    .timeline-period { color: #315efb; text-transform: uppercase;
        font-size: .7rem; letter-spacing: .12em; font-weight: 800; }
    .timeline-company { color: #15243a; font-size: 1.1rem; font-weight: 800;
        margin: .25rem 0; }
    .timeline-role { color: #526176; font-weight: 650; font-size: .9rem; }
    .timeline-copy { color: #64748b; font-size: .9rem; margin-top: .45rem; }

    .skill-chip {
        display: inline-block; background: #fff; border: 1px solid #e2e8f0;
        color: #34445d; padding: .48rem .78rem; border-radius: 10px;
        margin: .25rem .25rem .25rem 0; font-size: .84rem;
    }
    .contact-panel {
        background: #15243a; border-radius: 24px; padding: 2rem;
        color: white; margin-top: .5rem;
    }
    .contact-panel h2, .contact-panel p { color: white !important; }
    .contact-panel p { color: #c8d5e9 !important; }

    .footer {
        border-top: 1px solid #e2e8f0; padding-top: 1.2rem;
        margin-top: 3.5rem; color: #94a3b8; font-size: .8rem;
    }
    div.stButton > button, div.stLinkButton > a {
        border-radius: 10px; font-weight: 700; min-height: 2.65rem;
    }
    div.stButton > button[kind="primary"] {
        background: #315efb; border-color: #315efb;
    }
    @media (max-width: 700px) {
        .topline { align-items: flex-start; }
        .hero-panel { margin-top: 1rem; }
    }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# NAVIGATION
# =========================================================
st.markdown(
    """
    <div class="topline">
        <div class="brand">SARANGA<span>.</span> VINOD</div>
        <div class="topnote">Marketing · Brand · Consumer Insights</div>
    </div>
    """,
    unsafe_allow_html=True,
)

pages = ["Home", "About", "Projects", "Experience", "Skills", "Education", "Contact"]
if "page" not in st.session_state:
    st.session_state.page = "Home"

nav_cols = st.columns(len(pages))
for i, name in enumerate(pages):
    with nav_cols[i]:
        if st.button(name, key=f"nav_{name}", use_container_width=True,
                     type="primary" if st.session_state.page == name else "secondary"):
            st.session_state.page = name
            st.rerun()

st.markdown("---")
page = st.session_state.page

# =========================================================
# HOME
# =========================================================
if page == "Home":
    left, right = st.columns([1.55, 1], gap="large")
    with left:
        st.markdown('<div class="eyebrow">Marketing portfolio · 2026</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="hero-title">Turning consumer<br>insights into<br><span class="accent">brand impact.</span></div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-copy">I’m Saranga Vinod, a PGDM Marketing student with a Computer Science background. I explore how customer understanding, strategic thinking and technology can work together to solve marketing challenges.</div>',
            unsafe_allow_html=True,
        )
        st.write("")
        b1, b2 = st.columns([1, 1])
        with b1:
            if st.button("Explore my projects ↘", type="primary", use_container_width=True):
                st.session_state.page = "Projects"
                st.rerun()
        with b2:
            if st.button("More about me", use_container_width=True):
                st.session_state.page = "About"
                st.rerun()
    with right:
        st.markdown(
            """
            <div class="hero-panel">
                <div class="panel-label">My perspective</div>
                <div class="panel-big">Technology mindset.<br>Marketing lens.<br>Customer focus.</div>
                <div class="panel-foot">Research · Positioning · Strategy · Execution</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")
    st.markdown('<div class="section-kicker">Selected work</div><div class="section-heading">Projects I’m proud to share</div><div class="section-intro">A selection of marketing projects focused on brand strategy, consumer understanding and go-to-market thinking.</div>', unsafe_allow_html=True)

    card_cols = st.columns(2, gap="large")
    for i, project in enumerate(PROJECTS):
        with card_cols[i % 2]:
            st.markdown(
                f"""
                <div class="project-card">
                    <div class="project-number">{project['number']} / SELECTED PROJECT</div>
                    <div class="project-tag">{project['tag']}</div>
                    <div class="project-title">{project['title']}</div>
                    <div class="project-category">{project['category']}</div>
                    <div class="project-summary">{project['summary']}</div>
                    <div class="project-focus">{project['contribution']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.link_button("Explore repository ↗", project["repo"], use_container_width=True)
        if i % 2 == 0:
            st.write("")

    st.write("")
    st.markdown('<div class="section-kicker">At a glance</div>', unsafe_allow_html=True)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="info-card"><div class="info-label">Education</div><div class="info-title">PGDM · Marketing</div><div class="info-copy">FIIB · 2025–2027</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="info-card"><div class="info-label">Foundation</div><div class="info-title">Technology + Business</div><div class="info-copy">Computer Science and management education</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="info-card"><div class="info-label">Interests</div><div class="info-title">Brand & Growth</div><div class="info-copy">Digital marketing, consumer insights and sales</div></div>', unsafe_allow_html=True)

# =========================================================
# ABOUT
# =========================================================
elif page == "About":
    st.markdown('<div class="section-kicker">A little about me</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Curious about people.<br>Interested in why brands grow.</div>', unsafe_allow_html=True)
    st.write(
        "I’m pursuing a PGDM at FIIB, majoring in Marketing and minoring in Operations, "
        "after completing a BTech in Computer Science. This combination has shaped the "
        "way I approach business problems: I like to understand the people behind the data, "
        "look for patterns and turn findings into clear, practical recommendations."
    )
    st.write(
        "My project work has explored brand strategy, social media and content planning, "
        "consumer-focused campaigns and go-to-market strategy. Through internships and "
        "customer-facing work, I’m continuing to build my ability to communicate clearly, "
        "work with different stakeholders and connect strategy with execution."
    )
    st.write("")
    st.markdown("### What I’m interested in")
    for chip in ["Digital Marketing", "Brand Strategy", "Consumer Research", "Product Marketing",
                 "Sales & Customer Development", "Marketing Analytics"]:
        st.markdown(f'<span class="skill-chip">{chip}</span>', unsafe_allow_html=True)
    st.write("")
    st.info("My goal is to keep learning through practical work, customer understanding and measurable business outcomes.")

# =========================================================
# PROJECTS
# =========================================================
elif page == "Projects":
    st.markdown('<div class="section-kicker">Selected work</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Marketing ideas, made practical.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-intro">Explore each repository for the project material and details. The summaries below describe the focus of each project.</div>', unsafe_allow_html=True)

    for project in PROJECTS:
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-number">{project['number']} / CASE STUDY</div>
                <div class="project-tag">{project['tag']}</div>
                <div class="project-title">{project['title']}</div>
                <div class="project-category">{project['category']}</div>
                <div class="project-summary">{project['summary']}</div>
                <div class="project-focus">Focus: {project['contribution']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("View project on GitHub ↗", project["repo"])
        st.write("")

# =========================================================
# EXPERIENCE
# =========================================================
elif page == "Experience":
    st.markdown('<div class="section-kicker">Experience & involvement</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Learning by doing.</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-intro">A mix of marketing, customer-facing, technical and social-impact experience.</div>', unsafe_allow_html=True)

    for exp in EXPERIENCES:
        st.markdown(
            f"""
            <div class="timeline-card">
                <div class="timeline-period">{exp['period']}</div>
                <div class="timeline-company">{exp['company']}</div>
                <div class="timeline-role">{exp['role']}</div>
                <div class="timeline-copy">{exp['description']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.caption("Before publishing, verify all dates and descriptions and add any relevant outcomes you can confidently support.")

# =========================================================
# SKILLS
# =========================================================
elif page == "Skills":
    st.markdown('<div class="section-kicker">Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Skills I’m building and applying.</div>', unsafe_allow_html=True)
    left, right = st.columns(2, gap="large")
    with left:
        st.markdown("### Marketing & business")
        for chip in ["Strategic Marketing", "Brand Strategy", "Market Research", "Consumer Insights",
                     "Social Media Strategy", "Digital Marketing", "Relationship Building",
                     "Go-to-Market Planning", "Customer Understanding"]:
            st.markdown(f'<span class="skill-chip">{chip}</span>', unsafe_allow_html=True)
    with right:
        st.markdown("### Tools & technical")
        for chip in ["Canva", "Google Ads", "Meta Ads", "Excel", "Python", "C Programming",
                     "HTML & CSS", "Marketing Analytics"]:
            st.markdown(f'<span class="skill-chip">{chip}</span>', unsafe_allow_html=True)

    st.write("")
    st.markdown("### Working style")
    a, b, c = st.columns(3)
    with a:
        st.markdown('<div class="info-card"><div class="info-title">Research-led</div><div class="info-copy">Start with the customer, context and evidence.</div></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="info-card"><div class="info-title">Structured thinking</div><div class="info-copy">Break down a challenge into manageable parts.</div></div>', unsafe_allow_html=True)
    with c:
        st.markdown('<div class="info-card"><div class="info-title">Collaborative</div><div class="info-copy">Communicate ideas and learn from feedback.</div></div>', unsafe_allow_html=True)

# =========================================================
# EDUCATION
# =========================================================
elif page == "Education":
    st.markdown('<div class="section-kicker">Education & learning</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Building a business-and-technology foundation.</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">2025–2027</div>
            <div class="info-title">PGDM · Fortune Institute of International Business (FIIB)</div>
            <div class="info-copy">Major: Marketing · Minor: Operations</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown(
        """
        <div class="info-card">
            <div class="info-label">2020–2024</div>
            <div class="info-title">BTech · Computer Science</div>
            <div class="info-copy">Vimal Jyothi Engineering College</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("### Certifications & learning")
    for cert in [
        "Software Testing — NPTEL",
        "Business Analytics — Internshala",
        "Global Immersion Program — Vietnam",
    ]:
        st.markdown(f"- {cert}")

# =========================================================
# CONTACT
# =========================================================
elif page == "Contact":
    st.markdown(
        """
        <div class="contact-panel">
            <div class="section-kicker" style="color:#9db4ff;">Let’s connect</div>
            <h2 style="font-size:2.25rem; letter-spacing:-.05em; margin-bottom:.6rem;">
                Open to learning, collaboration and new opportunities.
            </h2>
            <p>Feel free to explore my work or connect with me professionally.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    contact_cols = st.columns(3)
    with contact_cols[0]:
        st.markdown('<div class="info-card"><div class="info-label">GitHub</div><div class="info-title">Projects & code</div><div class="info-copy">Explore my repositories and project work.</div></div>', unsafe_allow_html=True)
        st.link_button("Visit GitHub ↗", GITHUB_PROFILE, use_container_width=True)
    with contact_cols[1]:
        st.markdown('<div class="info-card"><div class="info-label">LinkedIn</div><div class="info-title">Professional profile</div><div class="info-copy">Connect with me on LinkedIn.</div></div>', unsafe_allow_html=True)
        if LINKEDIN_URL:
            st.link_button("Open LinkedIn ↗", LINKEDIN_URL, use_container_width=True)
        else:
            st.caption("Add your LinkedIn URL near the top of app.py.")
    with contact_cols[2]:
        st.markdown('<div class="info-card"><div class="info-label">Email</div><div class="info-title">Get in touch</div><div class="info-copy">For professional conversations and opportunities.</div></div>', unsafe_allow_html=True)
        if EMAIL_ADDRESS:
            st.link_button("Email me ↗", f"mailto:{EMAIL_ADDRESS}", use_container_width=True)
        else:
            st.caption("Add your professional email near the top of app.py.")

    if RESUME_URL:
        st.write("")
        st.link_button("View my resume ↗", RESUME_URL)

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        <strong>Saranga Vinod</strong> · Marketing Portfolio
        <span style="float:right;">Built with Streamlit</span>
    </div>
    """,
    unsafe_allow_html=True,
)


