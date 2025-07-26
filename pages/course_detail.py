import streamlit as st
from components.utils import get_base64_image

st.set_page_config(page_title="Course Detail", layout="wide", initial_sidebar_state="collapsed")

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

# The navigation and routing logic should be handled in app.py
# Removed redundant code for sidebar navigation and routing handler

st.markdown("""
    <style>
    .course-detail-page {
        padding: 40px;
        font-family: 'Segoe UI', sans-serif;
    }
    .course-detail-header {
        background-color: #333;
        color: white;
        padding: 20px;
        font-size: 24px;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        margin-bottom: 30px;
        border-radius: 8px;
    }
    .course-detail-content {
        display: flex;
        gap: 30px;
    }
    .course-intro-video {
        flex: 2;
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 8px;
    }
    .course-intro-video h2,
    .course-chapters h2 {
        color: #104e33;
        font-size: 20px;
        margin-bottom: 15px;
    }
    .video-placeholder {
        background-color: #000;
        height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 48px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .course-progress-bar {
        background-color: #e0e0e0;
        border-radius: 5px;
        height: 10px;
        margin-bottom: 10px;
    }
    .course-progress-fill {
        background-color: #fcb336;
        height: 100%;
        border-radius: 5px;
        width: 70%; /* Example progress */
    }
    .course-description-section p {
        font-size: 15px;
        line-height: 1.6;
        color: #333;
        margin-bottom: 10px;
    }
    .course-chapters {
        flex: 1;
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 8px;
    }
    .chapter-item {
        background-color: #ffffff;
        padding: 12px 15px;
        border-radius: 5px;
        margin-bottom: 10px;
        font-size: 15px;
        color: #333;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .course-actions {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 40px;
    }
    .action-button {
        background-color: #333;
        color: white !important;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
        transition: background-color 0.3s ease;
        flex: 1;
        text-align: center;
    }
    .action-button:hover {
        background-color: #555;
    }
    .back-to-courses {
        margin-top: 30px;
        text-align: center;
    }
    .back-to-courses a {
        color: #fcb336;
        font-weight: bold;
        text-decoration: none;
        font-size: 16px;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

query_params = st.query_params
course_title = query_params.get("course", "Course Detail")

chapters = [
    "Scientific Learning",
    "Classification of Living Beings",
    "Honey Bee",
    "Heredity",
    "Physiological Structure and Life Process",
    "Nature and Environment",
    "Motion and Force",
    "Pressure",
    "Heat",
    "Wave",
    "Electricity and Magnetism",
    "Universe",
    "Information and Communication Technology",
    "Classification of Elements",
    "Chemical Reaction",
    "Gases",
    "Metal and Non-metals",
    "Hydrocarbon and Its Compounds",
    "Chemicals Used in Daily Life"
]

# Get selected chapter from query params
selected_chapter = query_params.get("chapter", None)

# Short explanations for the first four chapters
chapter_explanations = {
    "Scientific Learning": "This chapter explores the fundamental principles and methodologies behind scientific inquiry, emphasizing critical thinking and experimentation.",
    "Classification of Living Beings": "Dive into the hierarchical system of classifying organisms, understanding the principles and importance of taxonomy in biology.",
    "Honey Bee": "Learn about the fascinating social structure, life cycle, and ecological role of honey bees, including their importance in pollination.",
    "Heredity": "Discover the basic principles of heredity, including genes, inheritance patterns, and how traits are passed from one generation to the next."
}

chapter_videos = {
    "Scientific Learning": "https://youtu.be/B-goshfJeiU?feature=shared",
    "Classification of Living Beings": "https://youtu.be/JzihOwFW3gI?feature=shared",
    "Honey Bee": "https://youtu.be/Zr9NI5PPDR0?feature=shared",
    "Heredity": "https://youtu.be/KtsqinIx1ME?feature=shared"
}

course_intro_videos = {
    "Class 10 Science": "https://youtu.be/eQOwJAaKQek"
}

# Determine which title and video to show
if selected_chapter and selected_chapter in chapters and selected_chapter in chapter_explanations:
    main_title = selected_chapter
    # Show a video placeholder box (empty, ready for video embed)
    video_url = chapter_videos.get(selected_chapter)
    if video_url:
        video_id = video_url.split('/')[-1].split('?')[0] # Extract video ID
        video_html = f'''<iframe width="100%" height="300" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    else:
        video_html = '<div class="video-placeholder" style="background:#000;display:flex;align-items:center;justify-content:center;height:300px;border-radius:8px;"></div>'
    is_chapter_page = True
    about_title = "About This Chapter"
    about_text = chapter_explanations.get(selected_chapter, "")
else:
    main_title = "INTRO VIDEO"
    course_intro_video_url = course_intro_videos.get(course_title)
    if course_intro_video_url:
        video_id = course_intro_video_url.split('/')[-1].split('?')[0]
        video_html = f'''<iframe width="100%" height="300" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'''
    else:
        video_html = '<div class="video-placeholder" style="background:#000;display:flex;align-items:center;justify-content:center;height:300px;border-radius:8px;"></div>'
    is_chapter_page = False
    about_title = "About This Course"
    about_text = f"This course provides a comprehensive overview of {course_title.lower()} covering fundamental concepts and advanced topics. Dive deep into interactive lessons and practical examples designed to enhance your understanding.\nLearn at your own pace with on-demand access to all course materials, including video lectures, reading materials, and quizzes. Earn a certificate upon completion."

chapters_html = "".join([
    f'<a href="/course_detail?course={course_title}&chapter={chapter}" style="text-decoration:none;">'
    f'<div class="chapter-item" style="{ 'background:#fcb336;color:white;' if chapter == selected_chapter else '' }">{chapter}</div></a>'
    for chapter in chapters
])

st.markdown(f"""
    <div class="course-detail-page">
        <div class="course-detail-header">
            <span>Course: {course_title}</span>
            <span>DETAIL</span>
        </div>
        <div class="course-detail-content">
            <div class="course-intro-video">
                <h2>{main_title}</h2>
                {video_html}
                <div class="course-progress-bar"><div class="course-progress-fill"></div></div>
                <p style="text-align: right; font-size: 14px; color: #666;">70% Completed</p>
                <div class="course-description-section">
                    <h3>{about_title}</h3>
                    <p>{about_text}</p>
                </div>
            </div>
            <div class="course-chapters" style="max-height: 400px; overflow-y: auto;">
                <h2>CHAPTERS</h2>
                {chapters_html}
            </div>
        </div>
        <div class="course-actions">
            <a href="#" class="action-button">DOWNLOAD VIDEO</a>
            <a href="#" class="action-button">{'SUMMARIZED PDF' if is_chapter_page else 'DOWNLOAD PDF'}</a>
            <a href="/interface" class="action-button">{'ASK A QUESTION' if is_chapter_page else 'SUMMARIZE COURSE'}</a>
        </div>
        <div class="back-to-courses">
            <a href="/courses" target="_self">⬅ Back to Courses</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 40px;">
    <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
</div>
""", unsafe_allow_html=True) 