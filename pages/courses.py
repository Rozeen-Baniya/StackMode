import streamlit as st
from components.utils import get_base64_image


st.set_page_config(page_title="Courses", layout="wide", initial_sidebar_state="collapsed")

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
    .course-page {
        padding: 40px;
        font-family: 'Segoe UI', sans-serif;
    }
    .course-page h1 {
        font-size: 32px;
        color: #104e33;
        margin-bottom: 30px;
    }
    .course-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        max-width: 80%; /* Takes 80% of the screen length */
        margin: 0 auto;
    }
    .course-card {
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        overflow: hidden;
        transition: transform 0.2s ease-in-out;
    }
    .course-card:hover {
        transform: translateY(-5px);
    }
    .course-image-placeholder {
        background-color: #e0e0e0;
        height: 180px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #666;
        font-size: 14px;
    }
    .course-content {
        padding: 20px;
    }
    .course-microcredential {
        font-size: 12px;
        color: #888;
        margin-bottom: 5px;
        text-transform: uppercase;
    }
    .course-title {
        font-size: 20px;
        font-weight: bold;
        color: #104e33;
        margin-bottom: 10px;
    }
    .course-rating {
        color: #ffc107; /* Gold color for stars */
        margin-bottom: 10px;
    }
    .course-ratings-count {
        font-size: 14px;
        color: #666;
        margin-left: 5px;
    }
    .course-description {
        font-size: 14px;
        color: #333;
        line-height: 1.5;
        margin-bottom: 20px;
    }
    .course-button {
        display: inline-block;
        background-color: #fcb336;
        color: white !important;
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
    }
    .course-button:hover {
        background-color: #e69d2e;
    }
    </style>
""", unsafe_allow_html=True)

courses_data = [
    {
        "microcredential": "Class 10",
        "title": "Class 10 Science",
        "stars": 5,
        "ratings_count": 500,
        "provider": "SkillBridge",
        "description": "A comprehensive course covering all topics of Class 10 Science, including Physics, Chemistry, and Biology.",
        "image_path": "images/science_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Mathematics",
        "stars": 4,
        "ratings_count": 450,
        "provider": "SkillBridge",
        "description": "Master fundamental mathematical concepts for Class 10, covering algebra, geometry, and trigonometry.",
        "image_path": "images/maths_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Optional Mathematics",
        "stars": 4,
        "ratings_count": 380,
        "provider": "SkillBridge",
        "description": "Explore advanced mathematical topics and problem-solving techniques for Class 10 Optional Mathematics.",
        "image_path": "images/opt_maths_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Account",
        "stars": 3,
        "ratings_count": 210,
        "provider": "SkillBridge",
        "description": "Learn the basics of accounting principles and practices essential for Class 10 students.",
        "image_path": "images/account_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Humanity",
        "stars": 5,
        "ratings_count": 300,
        "provider": "SkillBridge",
        "description": "Delve into the core concepts of humanity, including history, civics, and culture for Class 10.",
        "image_path": "images/humanities_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Social Studies",
        "stars": 4,
        "ratings_count": 400,
        "provider": "SkillBridge",
        "description": "A comprehensive study of social structures, political systems, and geographical aspects relevant to Class 10.",
        "image_path": "images/social_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Health, Population and Environment Education",
        "stars": 4,
        "ratings_count": 250,
        "provider": "SkillBridge",
        "description": "Understand key concepts in health, population dynamics, and environmental conservation for Class 10.",
        "image_path": "images/health_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Economics",
        "stars": 3,
        "ratings_count": 180,
        "provider": "SkillBridge",
        "description": "An introduction to economic principles, market functions, and national economic issues for Class 10.",
        "image_path": "images/economics_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Sanskrit",
        "stars": 4,
        "ratings_count": 150,
        "provider": "SkillBridge",
        "description": "Learn the fundamentals of Sanskrit language, grammar, and classical texts for Class 10.",
        "image_path": "images/sanskrit_cover.jpg"
    },
    {
        "microcredential": "Class 10",
        "title": "Class 10 Computer Science",
        "stars": 5,
        "ratings_count": 320,
        "provider": "SkillBridge",
        "description": "Discover basic computer concepts, programming fundamentals, and essential applications for Class 10.",
        "image_path": "images/computer_cover.jpg"
    }
]

if 'courses_data' not in st.session_state:
    st.session_state.courses_data = courses_data

if st.button("Add New Course"):
    st.session_state.add_new_course_form = not st.session_state.get('add_new_course_form', False)

if st.session_state.get('add_new_course_form', False):
    st.header("Add a New Course")
    with st.form("new_course_form", clear_on_submit=True):
        new_microcredential = st.selectbox("Class (Microcredential)", ["Class 10", "Microcredential", "Certification", "Specialization", "Course", "Workshop"])
        new_title = st.text_input("Subject (Title)")
        new_stars = st.slider("Ratings (1-5 Stars)", 1, 5, 3)
        new_description = st.text_area("Short Introduction (Description)")
        new_image_placeholder = st.text_input("Image Placeholder Text (e.g., 'New Course Image')")
        new_provider = st.text_input("Provider", value="SkillBridge")
        new_ratings_count = st.number_input("Number of Ratings", min_value=0, value=0)

        submitted = st.form_submit_button("Add Course")
        if submitted:
            if new_title and new_description:
                new_course = {
                    "microcredential": new_microcredential,
                    "title": new_title,
                    "stars": new_stars,
                    "ratings_count": new_ratings_count,
                    "provider": new_provider,
                    "description": new_description,
                    "image_placeholder": new_image_placeholder if new_image_placeholder else f"{new_title} Image"
                }
                st.session_state.courses_data.append(new_course)
                st.success(f"Course '{new_title}' added successfully!")
            else:
                st.error("Please fill in Subject (Title) and Short Introduction (Description).")

if st.session_state.courses_data:
    st.markdown(f"""
        <div class="course-page">
            <h1>📚 Our Courses</h1>
            <div class="course-grid">
    """, unsafe_allow_html=True)

    for course in st.session_state.courses_data:
        image_content = ""
        if "image_path" in course and course["image_path"]:
            try:
                img_data = get_base64_image(course["image_path"])
                image_content = f'<img src="data:image/png;base64,{img_data}" alt="{course.get("title", "Course Image")}" style="width:100%; height:100%; object-fit:cover; border-radius: 10px 10px 0 0;"/>'
            except FileNotFoundError:
                image_content = course.get("image_placeholder", "Image Not Found")
        else:
            image_content = course.get("image_placeholder", "Image Placeholder")

        st.markdown(f"""
                <div class="course-card">
                    <div class="course-image-placeholder" style="background-color: transparent;">{image_content}</div>
                    <div class="course-content">
                        <div class="course-microcredential">{course.get("microcredential", "Microcredential")}</div>
                        <div class="course-title">{course.get("title", "Course Title")}</div>
                        <div class="course-rating">{"★" * course.get("stars", 0)}{"☆" * (5 - course.get("stars", 0))}
                            <span class="course-ratings-count">{course.get("ratings_count", 0)} ratings at {course.get("provider", "Provider")}</span>
                        </div>
                        <div class="course-description">{course.get("description", "Master fundamental and advanced techniques to effectively control language models, from basic commands to sophisticated output manipulation and format control.")}</div>
                        <a href="/course_detail?course={course.get('title', 'Course Detail')}" class="course-button">Enroll Now</a>
                    </div>
                </div>
        """, unsafe_allow_html=True)

    st.markdown("""
            </div>
            <a href="/" style="color: #fcb336; font-weight: bold; margin-top: 30px; display: inline-block;">⬅ Back to Home</a>
        </div>
    """, unsafe_allow_html=True)
else:
    st.warning("No course data available.")

# Footer
st.markdown("""
<div style="background: #104e33; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-top: 40px;">
    <p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p>
</div>
""", unsafe_allow_html=True) 