# 📺 YouTube Transcript to Detailed Notes Converter

A simple and powerful **Streamlit web application** that extracts transcripts from YouTube videos and generates concise, structured notes using **Google Gemini AI**.

---

## 🚀 Features

* 🔗 Accepts any valid YouTube video URL
* 📜 Automatically extracts video transcripts
* 🌐 Supports English transcripts (fallback to other languages if unavailable)
* ✨ Generates summarized notes within ~250 words
* 🖼 Displays video thumbnail
* ⚡ Fast summarization using Gemini (`gemini-2.5-flash-lite`)

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **YouTube Transcript API**
* **python-dotenv**

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-notes-app.git
cd youtube-notes-app
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in the root directory and add your API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters a YouTube video link
2. The app extracts the video ID
3. Transcript is fetched using `YouTubeTranscriptApi`
4. Transcript is sent to **Google Gemini AI**
5. AI generates a structured summary
6. Summary is displayed in the Streamlit UI

---

## 📌 Example

**Input:**

```
https://www.youtube.com/watch?v=example
```

**Output:**

* Bullet-point summary of the video
* Clear and concise notes

---

## ⚠️ Error Handling

* Invalid YouTube URLs are handled
* Graceful fallback if transcript language is unavailable
* Displays user-friendly error messages

---

## 📁 Project Structure

```
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔮 Future Enhancements

* 🎯 Multiple summary formats (short, detailed, blog-style)
* 🌍 Translation support
* 💾 Export notes as PDF
* 🧩 Timestamp-based summaries

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.
