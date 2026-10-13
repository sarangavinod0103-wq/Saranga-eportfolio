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
