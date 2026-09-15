import streamlit as st

st.set_page_config(
    page_title="Saranga Vinod | Marketing Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Styling ----------
st.markdown("""
<style>
    .block-container {padding-top: 2.5rem; padding-bottom: 3rem; max-width: 1200px;}
    .hero {
        padding: 3rem 0 2rem 0;
    }
    .hero h1 {
        font-size: 3.6rem;
        line-height: 1.05;
        margin-bottom: .7rem;
    }
    .hero .tagline {
        font-size: 1.35rem;
        color: #555;
        max-width: 780px;
    }
    .pill {
        display: inline-block;
        padding: .35rem .75rem;
        border: 1px solid #ddd;
        border-radius: 999px;
        margin: .2rem .25rem .2rem 0;
        font-size: .9rem;
    }
    .project {
        border: 1px solid #e5e5e5;
        border-radius: 18px;
        padding: 1.4rem;
        height: 100%;
        background: #fff;
    }
    .project h3 {margin-top: 0;}
    .muted {color:#666;}
    .section-space {margin-top: 2.5rem;}
    .metric {
        border-left: 3px solid #222;
        padding-left: 1rem;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- Data ----------
projects = [
    {
        "title": "WishCare",
        "subtitle": "Social Media & Content Strategy",
        "description": "A social media and content marketing strategy covering consumer research, competitive analysis, campaign development, creator strategy and community engagement.",
        "role": "Marketing Strategy & Consumer Research",
        "github": "https://github.com/sarangavinod0103-wq/Wishcare-social-media-strategy",
    },
    {
        "title": "Lenskart Smart Glasses",
        "subtitle": "Brand & Go-to-Market Strategy",
        "description": "A strategic marketing project exploring how Lenskart can make smart glasses feel like a natural extension of everyday eyewear.",
        "role": "Consumer Insight, Positioning & GTM Strategy",
        "github": "https://github.com/sarangavinod0103-wq/lenskart-smart-glasses-strategy",
    },
    {
        "title": "VedaCare",
        "subtitle": "Brand Strategy & Digital Marketing",
        "description": "A herbal skincare brand strategy covering brand identity, product portfolio, STP and a digital marketing approach using the POEM framework.",
        "role": "Brand Strategy & Digital Marketing",
        "github": "https://github.com/sarangavinod0103-wq/vedacare-brand-strategy",
    },
    {
        "title": "Amul × Gen Z",
        "subtitle": "Marketing Strategy",
        "description": "A Gen Z-focused marketing strategy addressing brand relevance through product innovation, packaging, influencers, Q-commerce and retail experience.",
        "role": "Market Analysis & Consumer-focused Strategy",
        "github": "https://github.com/sarangavinod0103-wq/amul-gen-z-marketing-strategy",
    },
]

# ---------- Sidebar ----------
st.sidebar.title("Saranga Vinod")
st.sidebar.caption("Marketing Portfolio")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Projects", "Skills", "Experience", "Education & Certifications", "Contact"],
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Focus areas**")
st.sidebar.write("Digital Marketing")
st.sidebar.write("Brand Strategy")
st.sidebar.write("Consumer Insights")
st.sidebar.write("Sales & Customer Understanding")

# ---------- Home ----------
if page == "Home":
    st.markdown("""
    <div class="hero">
        <h1>Saranga Vinod</h1>
        <div class="tagline">
            PGDM Marketing student building practical skills in brand strategy,
            digital marketing, consumer research and customer-focused growth.
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("What I bring")
        st.write("A technology background combined with management education and hands-on marketing projects.")
    with c2:
        st.subheader("Current direction")
        st.write("Exploring opportunities in digital marketing and sales, with a strong interest in understanding customers and turning insights into actionable strategies.")

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
    st.subheader("Featured Projects")

    cols = st.columns(2)
    for i, p in enumerate(projects):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="project">
                <h3>{p["title"]}</h3>
                <p><strong>{p["subtitle"]}</strong></p>
                <p class="muted">{p["description"]}</p>
                <p><strong>My focus:</strong> {p["role"]}</p>
            </div>
            """, unsafe_allow_html=True)
            st.link_button("View GitHub Project →", p["github"], use_container_width=True)

    st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)
    st.subheader("A snapshot")
    a, b, c = st.columns(3)
    a.markdown('<div class="metric"><strong>4</strong><br>Featured marketing projects</div>', unsafe_allow_html=True)
    b.markdown('<div class="metric"><strong>PGDM</strong><br>Marketing major</div>', unsafe_allow_html=True)
    c.markdown('<div class="metric"><strong>Tech + Marketing</strong><br>Cross-functional foundation</div>', unsafe_allow_html=True)

# ---------- About ----------
elif page == "About":
    st.title("About Me")
    st.write("""
    I am a PGDM student specializing in Marketing, with a BTech background in Computer Science.
    My interests sit at the intersection of technology, marketing and consumer understanding.
    """)
    st.write("""
    Through academic projects, internships and practical assignments, I have worked on brand
    strategy, consumer research, social media strategy, go-to-market planning and customer-facing
    activities. I enjoy breaking down a business problem, understanding the consumer and turning
    insights into a practical marketing direction.
    """)
    st.subheader("Career interests")
    for item in ["Digital Marketing", "Brand & Marketing Strategy", "Consumer Research", "Sales & Customer Development"]:
        st.markdown(f'<span class="pill">{item}</span>', unsafe_allow_html=True)

# ---------- Projects ----------
elif page == "Projects":
    st.title("Projects")
    st.caption("A curated selection of academic and practical marketing work.")

    for p in projects:
        st.markdown(f"### {p['title']}")
        st.write(f"**{p['subtitle']}**")
        st.write(p["description"])
        st.write(f"**My contribution / focus:** {p['role']}")
        st.link_button("Open GitHub Repository →", p["github"])
        st.divider()

# ---------- Skills ----------
elif page == "Skills":
    st.title("Skills & Tools")

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Marketing")
        for s in ["Strategic Marketing", "Brand Strategy", "Market Research", "Consumer Insights", "Social Media Strategy", "Digital Marketing", "Relationship Building"]:
            st.markdown(f"- {s}")
    with c2:
        st.subheader("Tools & Technical")
        for s in ["Canva", "Google Ads", "Meta Ads", "Excel", "Python", "C Programming", "Marketing Analytics"]:
            st.markdown(f"- {s}")

    st.subheader("Strengths")
    st.write("Patience • Problem Solving • Research Orientation • Customer Understanding • Strategic Thinking")

# ---------- Experience ----------
elif page == "Experience":
    st.title("Experience")

    experiences = [
        ("Bajaj Capital — Corporate Internship Program", "Marketing / Sales", "Customer-facing experience involving mutual fund sales and SIP target achievement."),
        ("Unlimits", "Marketing & Design Thinking Intern", "Conducted 20+ user interviews, created empathy maps and proposed UI simplifications."),
        ("Udayan Care — Social Internship Program", "Social Impact", "Mentored 15+ children, supported career counselling and contributed to planning activities."),
        ("Tech Citi Software Consulting", "Technical Internship", "Worked on web pages using HTML and CSS."),
    ]

    for title, role, description in experiences:
        st.subheader(title)
        st.write(f"**{role}**")
        st.write(description)
        st.divider()

# ---------- Education & Certifications ----------
elif page == "Education & Certifications":
    st.title("Education & Certifications")

    st.subheader("Education")
    st.markdown("**PGDM — FIIB (Fortune Institute of International Business)**")
    st.write("2025–2027 • Major: Marketing • Minor: Operations")
    st.markdown("**BTech — Computer Science, Vimal Jyothi Engineering College**")
    st.write("2020–2024")

    st.subheader("Certifications & Learning")
    for c in [
        "Software Testing — NPTEL",
        "Business Analytics — Internshala",
        "Global Immersion Program — Vietnam",
    ]:
        st.markdown(f"- {c}")

# ---------- Contact ----------
elif page == "Contact":
    st.title("Let's Connect")
    st.write("I am open to opportunities, marketing projects and professional conversations.")

    st.markdown("### GitHub")
    st.link_button(
        "Visit my GitHub profile →",
        "https://github.com/sarangavinod0103-wq",
    )

    st.markdown("### LinkedIn")
    st.info("Add your LinkedIn profile URL here before publishing the portfolio.")

    st.markdown("### Email")
    st.info("Add your professional email address here before publishing the portfolio.")

    st.caption("Portfolio created with Streamlit.")
