import streamlit as st
from components.utils import get_base64_image


st.set_page_config(page_title="Talent Acquisition", layout="wide", initial_sidebar_state="collapsed")


# ---------- ROUTING HANDLER ----------
query_params = st.query_params
selected_video = query_params.get("video", None)
selected_page = query_params.get("page", None)

if selected_video:
    st.markdown(f"""
        <style>
            .video-page {{
                padding: 40px;
                font-family: 'Segoe UI', sans-serif;
            }}
            .video-page h1 {{
                font-size: 32px;
                color: #104e33;
            }}
        </style>
        <div class="video-page">
            <h1>🎬 Video: {selected_video.replace('-', ' ').title()}</h1>
            <p>This is a placeholder page for the video. You can later embed a real video here.</p>
            <a href="/" style="color: #fcb336; font-weight: bold;">⬅ Back to Gallery</a>
        </div>
    """, unsafe_allow_html=True)
    st.stop()
elif selected_page == "Home":
    pass # Allow the rest of app.py to render the home page content
elif selected_page == "About":
    st.switch_page("pages/about.py")
elif selected_page == "Services":
    st.write("🛠️ Services Page Content Here")
elif selected_page == "Contact":
    st.write("📞 Contact Page Content Here")
elif selected_page == "Courses":
    st.switch_page("pages/courses.py")
elif selected_page == "Course Detail":
    st.switch_page("pages/course_detail.py")
else:
    pass # Allow the rest of app.py to render the home page content by default

# ---------- BASE64 IMAGE UTILITY ----------

# ---------- NAV BAR ----------
logo_base64 = get_base64_image("images/logo.png")
st.markdown(f"""
    <style>
    .nav-container {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #fffced;
        color: #fcb336;
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
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
hero_bg = get_base64_image("images/hero.png")
st.markdown(f"""
    <style>
    .hero-section {{
        position: relative;
        height: 240px;
        background-image: linear-gradient(
            to right,
            rgba(252, 179, 54, 0.3),
            rgba(255, 252, 237, 0.85)
        ), url("data:image/png;base64,{hero_bg}");
        background-size: cover;
        background-position: center left;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-left: 80px;
        color: #104e33;
        font-family: 'Segoe UI', sans-serif;
    }}
    .breadcrumb {{
        font-size: 13px;
        text-transform: uppercase;
        color: #8c8c8c;
        margin-bottom: 8px;
        font-weight: 500;
        letter-spacing: 1px;
    }}
    .breadcrumb a {{
        color: #8c8c8c;
        text-decoration: none;
    }}
    .breadcrumb a:hover {{                                                                                              
        text-decoration: underline;
    }}
    .hero-title {{
        font-size: 32px;
        font-weight: 700;
        line-height: 1.3;
        text-shadow: 0px 1px 2px rgba(255,255,255,0.8);
    }}
    </style>
    <div class="hero-section">
        <div class="breadcrumb">
            <a href="#">HOME</a> &nbsp; 
        </div>
        <div class="hero-title">Unlock Your Potential,<br> Discover Your Future</div>
    </div>
""", unsafe_allow_html=True)

# ---------- STYLES FOR SUBJECT CARDS ----------
st.markdown("""
    <style>
    .subject-card {
        background-size: cover;
        background-position: center;
        border-radius: 15px;
        padding: 24px;
        height: 260px;
        color: #104e33;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        text-decoration: none;
    }

    .subject-card:hover {
        transform: scale(1.03);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    .subject-icon {
        position: absolute;
        top: 16px;
        left: 16px;
        width: 44px;
        height: 44px;
        background-color: rgba(255,255,255,0.85);
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        color: #104e33;
        font-weight: bold;
        box-shadow: 0 3px 8px rgba(0,0,0,0.2);
    }

    .subject-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 6px;
    }

    .subject-desc {
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- SUBJECT CARDS ----------
subject_info = [
    ("Science", "images/thumb1.jpg", "🔬"),
    ("Mathematics", "images/thumb2.jpg", "📐"),
    ("Technology", "images/thumb3.jpg", "💻"),
    ("Business", "images/thumb4.jpg", "📊")
]

subject_cards = []
for title, path, icon in subject_info:
    img_data = get_base64_image(path)
    card_html = f"""
        <a href="/courses" style="text-decoration: none;">
            <div class="subject-card" style="
                background-image: url('data:image/png;base64,{img_data}');
            ">
                <div class="subject-icon">{icon}</div>
                <div class="subject-title">{title}</div>
                <div class="subject-desc">Explore comprehensive courses in {title.lower()} and enhance your skills.</div>
            </div>
        </a>
    """
    subject_cards.append(card_html)

# ---------- LAYOUT ----------
col1, col2 = st.columns(2)
with col1:
    st.markdown(subject_cards[0], unsafe_allow_html=True)
    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
    st.markdown(subject_cards[2], unsafe_allow_html=True)
with col2:
    st.markdown(subject_cards[1], unsafe_allow_html=True)
    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
    st.markdown(subject_cards[3], unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <a href="/courses" target="_self" style="
            background-color: #fcb336;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 18px;
            transition: background-color 0.3s ease;
        ">View All Courses</a>
    </div>
""", unsafe_allow_html=True)

# ---------- RECRUITMENT EXCELLENCE SECTION ----------

recruitment_img = get_base64_image("images/recruitment.jpg")

st.markdown("""
    <style>
    .recruitment-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #fffced;
        padding: 60px 40px;
        border-radius: 20px;
        margin-top: 60px;
        font-family: 'Segoe UI', sans-serif;
    }

    .recruitment-left {
        flex: 1;
        padding-right: 40px;
    }

    .recruitment-left img {
        width: 100%;
        border-radius: 15px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.1);
    }

    .recruitment-right {
        flex: 1.2;
        color: #104e33;
    }

    .recruitment-subtitle {
        color: #fcb336;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 12px;
    }

    .recruitment-title {
        font-size: 28px;
        font-weight: 700;
        line-height: 1.3;
        margin-bottom: 20px;
    }

    .recruitment-desc {
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 20px;
        color: #333;
    }

    .recruitment-list {
        list-style: none;
        padding-left: 0;
        color: #104e33;
    }

    .recruitment-list li {
        margin-bottom: 12px;
        position: relative;
        padding-left: 28px;
        font-size: 15px;
    }

    .recruitment-list li::before {
        content: "✔";
        position: absolute;
        left: 0;
        color: #fcb336;
        font-weight: bold;
    }
    </style>
    <div class="recruitment-section">
        <div class="recruitment-left">
            <img src="data:image/png;base64,""" + recruitment_img + """" alt="Recruitment Excellence Image"/>
        </div>
        <div class="recruitment-right">
            <div class="recruitment-subtitle">RECRUITMENT EXCELLENCE</div>
            <div class="recruitment-title">Bridging Gaps<br>Sparkling Minds</div>
            <div class="recruitment-desc">
                We deliver top-tier recruitment services tailored to your specific business needs.
                Our process ensures you connect with high-performing professionals aligned with your goals.
            </div>
            <ul class="recruitment-list">
                <li>Access to industry-leading professionals</li>
                <li>Streamlined, proven hiring process</li>
                <li>Deep understanding of market trends</li>
                <li>Commitment to long-term talent success</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------- FOOTER SECTION ----------

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
    <div style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px;">
        <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
    </div>
""", unsafe_allow_html=True)
