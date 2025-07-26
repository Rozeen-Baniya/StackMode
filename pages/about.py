import streamlit as st
from components.utils import get_base64_image

# ---------- ABOUT US PAGE ----------
st.set_page_config(page_title="About Us", layout="wide", initial_sidebar_state="collapsed")

# ---------- NAV BAR ----------
logo_base64 = get_base64_image("images/logo.png")

# Get social media icons
facebook_icon = get_base64_image("images/facebook.png")
instagram_icon = get_base64_image("images/instagram.png")
twitter_icon = get_base64_image("images/twitter.png")
whatsapp_icon = get_base64_image("images/whatsapp.png")

# Navigation bar HTML
nav_html = f"""
<style>
.nav-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #fffced;
    color: #fcb336;
    margin-bottom: 0;
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
}}
.nav-right .cta-btn {{
    background-color: #fcb336;
    padding: 8px 16px;
    border-radius: 5px;
    color: white !important;
    font-weight: bold;
    text-decoration: none;
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

# Main content styles
main_styles = """
<style>
.about-hero {
    background: linear-gradient(135deg, #fcb336 0%, #f7931e 100%);
    padding: 80px 40px;
    text-align: center;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
}
.about-hero h1 {
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 20px;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.about-hero p {
    font-size: 20px;
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.6;
    opacity: 0.95;
}

.about-content {
    padding: 80px 40px;
    font-family: 'Segoe UI', sans-serif;
    max-width: 1200px;
    margin: 0 auto;
}

.mission-section {
    display: flex;
    align-items: center;
    gap: 60px;
    margin-bottom: 80px;
}

.mission-text {
    flex: 1;
}

.mission-text h2 {
    font-size: 36px;
    color: #104e33;
    margin-bottom: 20px;
    font-weight: 700;
}

.mission-text p {
    font-size: 18px;
    line-height: 1.8;
    color: #333;
    margin-bottom: 20px;
}

.mission-image {
    flex: 1;
    text-align: center;
}

.mission-image img {
    width: 100%;
    max-width: 400px;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.values-section {
    background-color: #f8f9fa;
    padding: 60px 40px;
    border-radius: 20px;
    margin: 40px 0;
}

.values-section h2 {
    text-align: center;
    font-size: 36px;
    color: #104e33;
    margin-bottom: 40px;
    font-weight: 700;
}

.values-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}

.value-card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}

.value-card:hover {
    transform: translateY(-5px);
}

.value-icon {
    font-size: 48px;
    margin-bottom: 20px;
}

.value-card h3 {
    font-size: 24px;
    color: #104e33;
    margin-bottom: 15px;
    font-weight: 600;
}

.value-card p {
    color: #666;
    line-height: 1.6;
}

.social-section {
    background: linear-gradient(135deg, #104e33 0%, #1a6b4a 100%);
    padding: 60px 40px;
    text-align: center;
    color: white;
    margin: 40px 0;
    border-radius: 20px;
}

.social-section h2 {
    font-size: 36px;
    margin-bottom: 20px;
    font-weight: 700;
}

.social-section p {
    font-size: 18px;
    margin-bottom: 40px;
    opacity: 0.9;
}

.social-icons {
    display: flex;
    justify-content: center;
    gap: 30px;
    flex-wrap: wrap;
}

.social-icon {
    width: 60px;
    height: 60px;
    background: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: #104e33;
    text-decoration: none;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.social-icon:hover {
    transform: scale(1.1);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.footer {
    background-color: #104e33;
    padding: 50px 40px;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    margin-top: 60px;
}

.footer-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    max-width: 1200px;
    margin: 0 auto;
}

.footer-col {
    flex: 1 1 200px;
    margin-right: 40px;
    margin-bottom: 30px;
}

.footer-col h4 {
    font-size: 16px;
    color: #fcb336;
    margin-bottom: 16px;
    font-weight: 700;
    text-transform: uppercase;
}

.footer-col ul {
    list-style: none;
    padding: 0;
}

.footer-col ul li {
    margin-bottom: 10px;
    font-size: 14px;
    color: #ddd;
}

.footer-col ul li:hover {
    color: #fcb336;
    cursor: pointer;
}

.footer-brand {
    font-size: 18px;
    font-weight: bold;
    color: white;
    margin-bottom: 12px;
}

.footer-desc {
    font-size: 14px;
    color: #ccc;
}
</style>
"""

# Hero section
hero_html = """
<div class="about-hero">
    <h1>About Us</h1>
    <p>Empowering rural communities through accessible, high-quality education and skill development opportunities.</p>
</div>
"""

st.markdown(main_styles, unsafe_allow_html=True)
st.markdown(hero_html, unsafe_allow_html=True)

# Mission section
mission_html = """
<div class="about-content">
    <div class="mission-section">
        <div class="mission-text">
            <h2>Our Mission</h2>
            <p>We are a dedicated e-learning platform committed to bridging the educational gap in rural areas. Our mission is to provide accessible, high-quality education to students who face geographical, economic, or infrastructural barriers to traditional learning.</p>
            <p>Through innovative technology and carefully curated content, we ensure that every student, regardless of their location, has access to world-class educational resources and the opportunity to develop essential skills for the modern workforce.</p>
        </div>
        <div class="mission-image">
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400&h=300&fit=crop" alt="Students learning online" />
        </div>
    </div>
"""

st.markdown(mission_html, unsafe_allow_html=True)

# Values section
values_html = """
    <div class="values-section">
        <h2>Our Core Values</h2>
        <div class="values-grid">
            <div class="value-card">
                <div class="value-icon">🌍</div>
                <h3>Accessibility</h3>
                <p>Making quality education available to everyone, regardless of location or economic status.</p>
            </div>
            <div class="value-card">
                <div class="value-icon">🎯</div>
                <h3>Excellence</h3>
                <p>Delivering high-quality, relevant content that meets international educational standards.</p>
            </div>
            <div class="value-card">
                <div class="value-icon">🤝</div>
                <h3>Community</h3>
                <p>Building supportive learning communities that foster collaboration and mutual growth.</p>
            </div>
            <div class="value-card">
                <div class="value-icon">💡</div>
                <h3>Innovation</h3>
                <p>Continuously improving our platform with cutting-edge technology and teaching methods.</p>
            </div>
        </div>
    </div>
"""

st.markdown(values_html, unsafe_allow_html=True)

# Social section
social_html = f"""
    <div class="social-section">
        <h2>Keep in Touch with Us</h2>
        <p>Follow us on social media for the latest updates, educational tips, and community stories.</p>
        <div class="social-icons">
            <a href="#" class="social-icon"><img src="data:image/png;base64,{facebook_icon}" alt="Facebook" style="width: 24px; height: 24px;"></a>
            <a href="#" class="social-icon"><img src="data:image/png;base64,{instagram_icon}" alt="Instagram" style="width: 24px; height: 24px;"></a>
            <a href="#" class="social-icon"><img src="data:image/png;base64,{twitter_icon}" alt="Twitter" style="width: 24px; height: 24px;"></a>
            <a href="#" class="social-icon"><img src="data:image/png;base64,{whatsapp_icon}" alt="WhatsApp" style="width: 24px; height: 24px;"></a>
        </div>
    </div>
</div>
"""

st.markdown(social_html, unsafe_allow_html=True)

# Footer
st.markdown("""
    <style>
    .footer {
        background-color: #104e33;
        padding: 50px 40px;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        margin-top: 60px;
    }

    .footer-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .footer-col {
        flex: 1 1 200px;
        margin-right: 40px;
        margin-bottom: 30px;
    }

    .footer-col h4 {
        font-size: 16px;
        color: #fcb336;
        margin-bottom: 16px;
        font-weight: 700;
        text-transform: uppercase;
    }

    .footer-col ul {
        list-style: none;
        padding: 0;
    }

    .footer-col ul li {
        margin-bottom: 10px;
        font-size: 14px;
        color: #ddd;
    }

    .footer-col ul li:hover {
        color: #fcb336;
        cursor: pointer;
    }
    .footer-col ul li a:hover {
        color: #fcb336;
        cursor: pointer;
    }

    .footer-brand {
        font-size: 18px;
        font-weight: bold;
        color: #fcb336;
        margin-bottom: 12px;
    }

    .footer-desc {
        font-size: 14px;
        color: #ccc;
    }
    </style>

    <div class="footer">
        <div class="footer-container">
            <div class="footer-col">
                <div class="footer-brand">SkillBridge</div>
                <div class="footer-desc">
                    Empowering rural communities through accessible, high-quality education and skill development opportunities.
                </div>
            </div>
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul>
                    <li><a href="/" style="color: #ddd; text-decoration: none;">Homepage</a></li>
                    <li><a href="/about" style="color: #ddd; text-decoration: none;">About Us</a></li>
                    <li><a href="/services" style="color: #ddd; text-decoration: none;">Our Services</a></li>
                    <li><a href="/courses" style="color: #ddd; text-decoration: none;">Our Courses</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Our Services</h4>
                <ul>
                    <li>Personal Mentorship</li>
                    <li>Study Materials</li>
                    <li>AI Assistance</li>
                    <li>SMS Support</li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Contact Information</h4>
                <ul>
                    <li>📧 info@skillbridge.com</li>
                    <li>📞 +1 (234) 567-8900</li>
                    <li>📍 Rural Education Center</li>
                    <li>🌐 www.skillbridge.com</li>
                </ul>
            </div>
        </div>
    </div>
    
    <!-- Copyright Footer -->
    <style>
        .Copyright Footer:hover {
            color: #fcb336;
            cursor: pointer;
    </style>  
    <div class="Copyright Footer" style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px;">
        <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
    </div>
""", unsafe_allow_html=True)


