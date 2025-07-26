import streamlit as st
from components.utils import get_base64_image

# ---------- SERVICES PAGE ----------
st.set_page_config(page_title="Our Services", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for styling
st.markdown("""
<style>
    /* Main page styling */
    .main-header {
        background: linear-gradient(135deg, #104e33 0%, #1a6b4a 100%);
        padding: 40px 20px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
        color: white;
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .main-header h3 {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 400;
    }
    
    /* Service cards styling */
    .service-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #fcb336;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .service-icon {
        font-size: 2.5rem;
        margin-bottom: 15px;
        display: block;
    }
    
    .service-title {
        color: #104e33;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .service-description {
        color: #666;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    
    .service-features {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        margin: 15px 0;
    }
    
    .service-features ul {
        margin: 0;
        padding-left: 20px;
    }
    
    .service-features li {
        color: #555;
        margin: 8px 0;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #fcb336 0%, #f7931e 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 25px;
        font-weight: 600;
        transition: transform 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #f7931e 0%, #e67e22 100%);
    }
    
    /* CTA section styling */
    .cta-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 40px 20px;
        border-radius: 15px;
        text-align: center;
        margin: 30px 0;
        border: 2px solid #e9ecef;
    }
    
    .cta-title {
        color: #104e33;
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 15px;
    }
    
    .cta-description {
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    
    /* Contact section styling */
    .contact-section {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin: 30px 0;
    }
    
    .contact-title {
        color: #104e33;
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .contact-info {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 20px;
    }
    
    .contact-item {
        text-align: center;
        padding: 15px;
        background: #f8f9fa;
        border-radius: 10px;
        min-width: 200px;
    }
    
    .contact-icon {
        font-size: 1.5rem;
        margin-bottom: 10px;
        display: block;
    }
    
    .contact-text {
        color: #555;
        font-weight: 500;
    }
    
    /* Footer styling */
    .footer {
        background: #104e33;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 30px;
    }
    
    /* Divider styling */
    .divider {
        height: 3px;
        background: linear-gradient(90deg, #fcb336, #f7931e);
        border-radius: 2px;
        margin: 30px 0;
    }
    
    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------- NAV BAR ----------
logo_base64 = get_base64_image("images/logo.png")

# Simple navigation bar
nav_html = f"""
<style>
.nav-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #fffced;
    color: #fcb336;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}}
.nav-left {{
    font-size: 24px;
    font-weight: bold;
    display: flex;
    align-items: center;
}}
.nav-logo {{
    width: 60px;
    margin-right: 12px;
}}
.nav-right a {{
    margin-left: 20px;
    color: #fcb336;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}}
.nav-right a:hover {{
    color: #f7931e;
}}
.nav-right .cta-btn {{
    background-color: #fcb336;
    padding: 8px 16px;
    border-radius: 5px;
    color: white !important;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s ease;
}}
.nav-right .cta-btn:hover {{
    background-color: #f7931e;
}}
</style>
<div class="nav-container">
    <div class="nav-left">
        <img class="nav-logo" src="data:image/png;base64,{logo_base64}" alt="SkillBridge" />
        <span>SkillBridge</span>
    </div>
    <div class="nav-right">
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/services">Services</a>
        <a href="/contact">Contact</a>
        <a href="/courses">Courses</a>
        <a class="cta-btn" href="tel:+1234566789">📞 9842519032</a>
    </div>
</div>
"""

st.markdown(nav_html, unsafe_allow_html=True)

# Page Header with custom styling
st.markdown("""
<div class="main-header">
    <h1>Our Services</h1>
    <h3>Comprehensive learning solutions for rural communities</h3>
</div>
""", unsafe_allow_html=True)

# Services Introduction
st.markdown("""
<div style="text-align: center; padding: 20px; background: #f8f9fa; border-radius: 10px; margin: 20px 0;">
    <p style="font-size: 1.1rem; color: #555; line-height: 1.6;">
        We provide a comprehensive suite of educational services designed to bridge the gap between traditional learning and modern technology, ensuring every student has access to quality education regardless of their location.
    </p>
</div>
""", unsafe_allow_html=True)

# Services Grid using columns
col1, col2 = st.columns(2)

with col1:
    # Personal Mentorship
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">👨‍🏫</span>
        <div class="service-title">Personal Mentorship</div>
        <div class="service-description">
            Get personalized guidance from experienced educators who understand your learning journey and provide tailored support to help you achieve your educational goals.
        </div>
        <div class="service-features">
            <ul>
                <li>One-on-one mentoring sessions</li>
                <li>Personalized learning plans</li>
                <li>Regular progress tracking</li>
                <li>Career guidance and counseling</li>
                <li>24/7 mentor availability</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Get Started", key="mentorship"):
        st.success("🎉 Contact us to get started with personal mentorship!")
    
    # Study Materials
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📚</span>
        <div class="service-title">Study Materials</div>
        <div class="service-description">
            Access comprehensive, up-to-date study materials curated by experts, including textbooks, practice tests, video lectures, and interactive content.
        </div>
        <div class="service-features">
            <ul>
                <li>Comprehensive course materials</li>
                <li>Practice tests and quizzes</li>
                <li>Video lectures and tutorials</li>
                <li>Interactive learning modules</li>
                <li>Offline download capability</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Browse Materials", key="materials"):
        st.success("📖 Explore our comprehensive study materials!")

with col2:
    # AI Assistance
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">🤖</span>
        <div class="service-title">AI Assistance</div>
        <div class="service-description">
            Leverage cutting-edge artificial intelligence to get instant help with your studies, homework, and technical questions through our smart learning assistant.
        </div>
        <div class="service-features">
            <ul>
                <li>24/7 AI-powered tutoring</li>
                <li>Instant homework help</li>
                <li>Step-by-step explanations</li>
                <li>Adaptive learning paths</li>
                <li>Multi-language support</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Try AI Assistant", key="ai"):
        st.success("🚀 Experience our AI-powered learning assistant!")
    
    # SMS Assistance
    st.markdown("""
    <div class="service-card">
        <span class="service-icon">📱</span>
        <div class="service-title">SMS Assistance</div>
        <div class="service-description">
            Get quick technical support and answers to your questions via SMS, ensuring you never get stuck even when internet connectivity is limited.
        </div>
        <div class="service-features">
            <ul>
                <li>Quick SMS-based support</li>
                <li>Technical issue resolution</li>
                <li>Study tips and reminders</li>
                <li>Emergency assistance</li>
                <li>Low-cost communication</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Send SMS", key="sms"):
        st.success("📱 Send us an SMS for quick support!")

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="cta-section">
    <div class="cta-title">Ready to Start Your Learning Journey?</div>
    <div class="cta-description">Join thousands of students who are already benefiting from our comprehensive educational services.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    pass

with col2:
    if st.button("Start Learning Now", type="primary", use_container_width=True):
        st.balloons()
        st.success("🎓 Welcome to SkillBridge! Let's begin your learning journey.")

with col3:
    pass

# Contact Information
st.markdown("""
<div class="contact-section">
    <div class="contact-title">Contact Us</div>
    <div class="contact-info">
        <div class="contact-item">
            <span class="contact-icon">📧</span>
            <div class="contact-text">info@skillbridge.com</div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">📞</span>
            <div class="contact-text">+1 (234) 567-8900</div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">📍</span>
            <div class="contact-text">Rural Education Center</div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">🌐</span>
            <div class="contact-text">www.skillbridge.com</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 40px;">
    <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
</div>
""", unsafe_allow_html=True) 