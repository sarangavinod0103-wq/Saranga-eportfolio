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
