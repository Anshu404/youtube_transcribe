# 📺 YouTube Transcript Summarizer App

A Streamlit web application that takes a **YouTube video link**, extracts the transcript using `youtube-transcript-api`, and provides a **clean, concise summary** using a powerful language model (e.g., Gemini Pro or GPT).

---

## 🚀 Features

- 🎥 Input any public YouTube video link
- 📝 Auto-fetch the full transcript using the YouTube Transcript API
- 🤖 Summarize using Google Gemini / OpenAI GPT
- 🌐 Easy-to-use web UI powered by Streamlit
- 🔐 Environment-safe with `.env` support for API keys

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-transcript-summarizer.git
cd youtube-transcript-summarizer
2. Install Required Packages
Make sure you’re using Python 3.8+.

bash
Copy
Edit
pip install -r requirements.txt
Or manually:

bash
Copy
Edit
pip install streamlit python-dotenv youtube-transcript-api google-generativeai
Replace google-generativeai with openai if you're using GPT instead.

3. Set Up Your .env File
Create a file called .env in the root directory and add your API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
# or
OPENAI_API_KEY=your_openai_api_key_here
4. Run the App
bash
Copy
Edit
streamlit run app.py
App will be live at: http://localhost:8501

📁 File Structure
bash
Copy
Edit
.
├── app.py
├── .env
├── README.md
├── requirements.txt


📦 requirements.txt Example
nginx
Copy
Edit
streamlit
python-dotenv
youtube-transcript-api
google-generativeai
# or openai if using GPT
🙋‍♂️ Author
Anshu Mandal
Data Science @ IIT Mandi

🧠 License
Licensed under the MIT License — feel free to use and modify.

🌍 Optional Deployment
You can deploy this app on:

Streamlit Cloud

Render

Railway

❓ Want More Features?
🔊 Add speech-to-text for non-captioned videos?

📤 Export summaries as PDFs?

📂 Summarize entire playlists?
