import streamlit as st
import chromadb
from chromadb.config import Settings
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import os # Import os module
from components.utils import get_base64_image

st.set_page_config(page_title="Interface", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    html, body, .main, .block-container {
        height: 100%;
        min-height: 100vh;
    }
    body {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        background-color: #fffced;
    }
    .page-wrapper {
        flex: 1 0 auto;
        display: flex;
        flex-direction: column;
        min-height: 80vh;
    }
    .st-emotion-cache-s8s0g3 {
        display: none;
    }
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    .main-header {
        font-size: 36px;
        font-weight: bold;
        color: #333;
        text-align: center;
        margin-bottom: 50px;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        background: none;
        margin-top: 40px;
    }
    .input-container {
        display: flex;
        gap: 20px;
        margin-bottom: 20px;
        justify-content: center;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
    }
    .input-field {
        border: 1px solid #000;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
        flex-grow: 1;
    }
    .large-text-area {
        border: 1px solid #000;
        border-radius: 15px;
        padding: 20px;
        height: 250px;
        margin-bottom: 30px;
        overflow-y: auto;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        box-sizing: border-box;
    }
    .query-input-container {
        display: flex;
        gap: 20px;
        align-items: center;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
    }
    .query-input {
        border: 1px solid #000;
        border-radius: 25px;
        padding: 10px 20px;
        font-size: 16px;
        flex-grow: 1;
    }
    .send-button {
        background-color: #000;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        font-size: 16px;
        cursor: pointer;
    }
    .stTextInput>div>div>input {
        border: 1px solid #000;
        border-radius: 25px;
        padding: 10px 20px;
    }
    .stTextArea>div>div>textarea {
        border: 1px solid #000;
        border-radius: 15px;
        padding: 20px;
        height: 250px;
    }
    .stButton>button {
        background-color: #000;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        font-size: 16px;
        cursor: pointer;
        width: 100%;
    }
    .nav-container {
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        border-radius: 0 !important;
    }
    .footer-fullwidth {
        flex-shrink: 0;
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        background: #104e33;
        color: white;
        padding: 20px;
        border-radius: 0 0 15px 15px;
        text-align: center;
        margin-top: 40px;
        box-sizing: border-box;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# CONFIGURE GEMINI
# -----------------------------
# Replace with your real key
GEMINI_API_KEY = "AIzaSyCxZjawkUvho7Wy9U50zNLM-vpBq_U5OgA" # You'll need to re-add your key here
genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# SETUP / LOAD VECTOR DATABASE
# -----------------------------
@st.cache_resource
def setup_chroma(_ = None): # Added a dummy parameter to force cache invalidation
    with st.spinner("Loading AI model and database..."):
        model = SentenceTransformer("all-MiniLM-L6-v2")
        chroma_client = chromadb.PersistentClient(path=".chroma")
        collection = chroma_client.get_or_create_collection(name="science-book")

        if not collection.count():
            with st.spinner("Embedding text for the first time... This might take a moment."):
                # Construct robust absolute path to science_grade10.txt
                script_dir = os.path.dirname(__file__)
                science_file_path = os.path.abspath(os.path.join(script_dir, os.pardir, 'science_grade10.txt'))
                
                with open(science_file_path, "r", encoding="utf-8") as f:
                    text = f.read()
                words = text.split()
                for i in range(0, len(words), 450):  # 500-word chunks with 50-overlap
                    chunk = " ".join(words[i:i+500])
                    embedding = model.encode(chunk).tolist()
                    collection.add(documents=[chunk], embeddings=[embedding], ids=[str(i)])
                st.success("✅ Text embedded and stored in vector DB.")
    return model, collection

# -----------------------------
# GET TOP CHUNKS FOR QUERY
# -----------------------------
def query_chunks(query, model, collection, top_k=3):
    query_vec = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=top_k)
    return results["documents"][0]

# -----------------------------
# GENERATE GEMINI RESPONSE
# -----------------------------
def generate_answer_with_gemini(query, chunks):
    context = "\n\n".join(chunks)
    prompt = f"""
You are a helpful AI tutor.

Use the following textbook content to answer the question clearly and accurately.

Context:
{context}

Question: {query}
"""
    response = gemini_model.generate_content(prompt)
    return response.text

# ---------- NAV BAR ----------
logo_base64 = get_base64_image("images/logo.png")

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

st.markdown("<div class='main-header'>Ask SkillBridge</div>", unsafe_allow_html=True)

response_placeholder = st.empty() # Placeholder for the response/chat history

# Main chat input at the bottom
col_query, col_send = st.columns([4, 1])
with col_query:
    query = st.text_input("", label_visibility="collapsed", placeholder="Write your query...", key="interface_query_input")
with col_send:
    if st.button("Send", key="interface_send_button"):
        if not query.strip():
            response_placeholder.markdown("<div class='large-text-area'>❗ Please enter a question first.</div>", unsafe_allow_html=True)
        else:
            with st.spinner("Thinking..."):
                embed_model, collection = setup_chroma(1) # Pass a dummy argument to force cache invalidation
                chunks = query_chunks(query, embed_model, collection)
                answer = generate_answer_with_gemini(query, chunks)

                response_placeholder.markdown(f"<div class='large-text-area'>{answer}</div>", unsafe_allow_html=True) 

st.markdown('<div class="page-wrapper">', unsafe_allow_html=True)
# Footer
st.markdown('</div>', unsafe_allow_html=True)  # Close .page-wrapper
st.markdown('<div class="footer-fullwidth"><p style="margin: 0; font-size: 1rem;">© 2024 SkillBridge. Empowering rural communities through accessible, high-quality education.</p></div>', unsafe_allow_html=True) 