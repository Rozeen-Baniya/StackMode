import streamlit as st
from components.utils import get_base64_image

# ---------- CONTACT PAGE ----------
st.set_page_config(page_title="Contact Us", layout="wide", initial_sidebar_state="collapsed")

# ---------- NAV BAR ----------
logo_base64 = get_base64_image("images/logo.png")

# Navigation bar
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

# Custom CSS for styling
st.markdown("""
<style>
    .contact-hero {
        background: linear-gradient(135deg, #104e33 0%, #1a6b4a 100%);
        padding: 60px 40px;
        text-align: center;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        border-radius: 15px;
        margin-bottom: 40px;
    }
    
    .contact-hero h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 15px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .contact-hero p {
        font-size: 1.2rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .contact-content {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }
    
    .contact-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 40px;
        margin-bottom: 40px;
    }
    
    .contact-info {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .contact-info h2 {
        color: #104e33;
        font-size: 1.8rem;
        margin-bottom: 20px;
        font-weight: 700;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        margin-bottom: 20px; /* Increased to make height equal */
        padding: 25px 15px; /* Increased vertical padding */
        background: #f8f9fa;
        border-radius: 10px;
        transition: transform 0.3s ease;
    }
    
    .contact-item:last-child {
        margin-bottom: 0; /* Remove margin from the last item */
    }
    
    .contact-item:hover {
        transform: translateX(5px);
    }
    
    .contact-icon {
        font-size: 1.5rem;
        margin-right: 15px;
        color: #fcb336;
    }
    
    .contact-text {
        color: #555;
        font-weight: 500;
    }
    
    .contact-form {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .contact-form h2 {
        color: #104e33;
        font-size: 1.8rem;
        margin-bottom: 20px;
        font-weight: 700;
    }
    
    .form-group {
        margin-bottom: 20px;
    }
    
    .form-group label {
        display: block;
        margin-bottom: 5px;
        color: #104e33;
        font-weight: 600;
    }
    
    .form-group input,
    .form-group textarea {
        width: 100%;
        padding: 12px;
        border: 2px solid #e9ecef;
        border-radius: 8px;
        font-size: 16px;
        transition: border-color 0.3s ease;
    }
    
    .form-group input:focus,
    .form-group textarea:focus {
        outline: none;
        border-color: #fcb336;
    }
    
    .submit-btn {
        background: linear-gradient(135deg, #fcb336 0%, #f7931e 100%);
        color: white;
        padding: 12px 30px;
        border: none;
        border-radius: 25px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .submit-btn:hover {
        transform: scale(1.05);
    }
    
    .footer {
        background: #104e33;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class="contact-hero">
    <h1>Contact Us</h1>
    <p>Get in touch with us for any questions about our services, courses, or to start your learning journey.</p>
</div>
""", unsafe_allow_html=True)

# Contact content
st.markdown("""
<div class="contact-content">
""", unsafe_allow_html=True)

# Contact grid
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="contact-info">
        <h2>Get in Touch</h2>
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
            <div class="contact-text">Rural Education Center<br>123 Learning Street<br>Education City, EC 12345</div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">🌐</span>
            <div class="contact-text">www.skillbridge.com</div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">⏰</span>
            <div class="contact-text">Monday - Friday: 8 AM - 10 PM<br>Saturday: 9 AM - 6 PM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-form">
        <h2>Send us a Message</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    with st.form("contact_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email Address *")
        phone = st.text_input("Phone Number")
        subject = st.selectbox("Subject *", ["General Inquiry", "Course Information", "Technical Support", "Partnership", "Other"])
        message = st.text_area("Message *", height=150)
        
        submitted = st.form_submit_button("Send Message", type="primary")
        
        if submitted:
            if name and email and message:
                st.success("🎉 Thank you for your message! We'll get back to you soon.")
            else:
                st.error("Please fill in all required fields marked with *")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 40px;">
    <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
</div>
""", unsafe_allow_html=True) 