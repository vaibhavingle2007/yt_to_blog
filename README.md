# 📝 YouTube to Blog Converter

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-orange)](https://streamlit.io/)
[![Deployed with Bolt](https://img.shields.io/badge/Deploy-Bolt-black)](https://bolt.new)

> 🚀 **AI-Powered Blog Generator** - Converts YouTube videos into summarized blog posts using AI transcription and NLP.

---

## 🎯 Project Overview

This application allows users to input any YouTube video link and get a readable, summarized blog version of the video. It uses AI models for transcription and summarization, making it easier to repurpose video content into articles.

---

## ✨ Features

- 🔗 **YouTube Link Input** – Paste a video URL to start
- 🧠 **AI Transcription** – Uses Whisper or DeepSeek for accurate audio-to-text
- ✍️ **Blog Generation** – Generates structured, readable blog content from video speech
- 🌐 **Multilingual Support** – Supports multiple languages (if configured)
- 🎨 **Minimal UI** – Easy to use web interface built for speed
- 💡 **Download Blog** – Export blog as `.txt` or `.md`
- 📸 **Thumbnail & Title Fetching** – Displays metadata from the video

---

## 🏗️ Project Structure

```

youtube-to-blog/
├── backend/                # FastAPI-based backend for processing
│   └── main.py            # API endpoints
├── frontend/               # Frontend (can be Streamlit, React, or HTML+JS)
│   └── app.py / index.html # Web interface
├── utils/                 # Transcription & blog logic
├── requirements.txt       # Backend dependencies
└── README.md              # This file

````

---

## 🚀 Quick Start

### 🔧 Prerequisites
- Python 3.10+
- Node.js (if using React)
- Git

### 🛠️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/youtube-to-blog.git
cd youtube-to-blog
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the FastAPI backend**

```bash
uvicorn backend.main:app --reload
```

4. **Start the frontend**

* If using **Streamlit**:

  ```bash
  streamlit run frontend/app.py
  ```
* If using **HTML/JS**:

  * Open `index.html` in browser
  * Make sure API is running at `http://localhost:8000`

---

## 🛠️ Tech Stack

### Backend

* **FastAPI** – API Framework
* **Python** – Core logic
* **Whisper / DeepSeek / Nebius** – For transcription
* **OpenAI / DeepSeek LLM** – For blog summarization

### Frontend (Option 1: Streamlit)

* **Streamlit** – Quick Python UI
* **Bootstrap** – Optional styling

### Frontend (Option 2: HTML + JS)

* **Vanilla JS / Tailwind CSS** – Lightweight, custom UI
* **Fetch API** – To hit backend endpoints

---

## 🎮 How to Use

1. Paste the YouTube video URL in the input field.
2. Click “Generate Blog”.
3. Wait for transcription & summary to complete.
4. View or download the blog article.

---

## 📋 Week 1 Deliverables ✅

* [x] **Day 1**: Setup backend & test script
* [x] **Day 2**: Build frontend layout
* [x] **Day 3**: Connect API with frontend
* [x] **Day 4**: Add loading, metadata, and error handling
* [x] **Day 5**: Polish UI and blog formatting
* [x] **Day 6**: Deploy using Bolt / Render / Railway
* [x] **Day 7**: Final testing & documentation

---

## 🔮 Future Roadmap

* 🌍 **Multi-language blog output**
* 🧠 **Topic detection for better structuring**
* 🖼️ **Auto-thumbnail generation**
* 🧵 **Thread writer / Twitter export**
* 📱 **Mobile responsive frontend**

---

## 🤝 Contributing

Got ideas or want to help improve the app?

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a pull request


<div align="center">

**Made with ❤️ using [Bolt.new](https://bolt.new)**

*Improving accessibility, one gesture at a time* 🤟

</div> 
```
