# 📦 StackMode

**StackMode** is a modern, multi-page web application built with [Streamlit](https://streamlit.io/). It provides a clean, modular, and image-rich UI — ideal for educational, recruitment, or service-based platforms.

---

## 🚀 Features

- 🌐 Multi-page navigation with custom navbar
- 🧩 Modular Streamlit structure (`components`, `pages`)
- 🎨 Visually appealing layout using custom images
- 📄 About and Courses pages already implemented
- ⚡ Quick setup and launch with `streamlit run`

---

## 🛠️ Tech Stack

- **Language**: Python 3.11+
- **Framework**: [Streamlit](https://streamlit.io/)
- **Assets**: Static images and modular components

---

## 📂 Project Structure

```
StackMode/
├── app.py                  # Main entry point for the Streamlit app
├── components/
│   └── navbar.py           # Custom navigation bar
├── pages/
│   ├── about.py            # 'About Us' page
│   └── courses.py          # 'Courses' page
├── images/                 # Static images used across the site
└── README.md               # Project documentation
```

---

## 🚧 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rozeen-Baniya/StackMode.git
   cd StackMode
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📸 Screenshots

<!-- Add screenshots here -->
> 📌 You can include preview images or GIFs of the app UI once available.

---

## 🧭 Roadmap / Ideas

- [ ] Add user login/authentication
- [ ] Add form submissions or contact page
- [ ] Connect to database for dynamic data
- [ ] Deploy to Streamlit Cloud / Hugging Face Spaces

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/)
- All open-source contributors
