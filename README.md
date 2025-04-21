# 🪷 Aikya Translate — One Voice, All Languages

**Aikya (एक्य)** means *unity* — and that’s exactly what this smart AI agent brings: seamless translation across all Indian languages, powered by GPT-4o.

Whether you say "Translate it to Tamil" or "Give this to me in Hindi," Aikya understands natural commands, detects your input language, and responds in the Indian language you need. It's like talking to your multilingual friend — fast, intelligent, and always ready.

---

## ✨ Features

- 🧠 **Conversational Input Detection**  
  Understands prompts like:
  - “Translate this to Telugu: I am learning AI”
  - “He said 'मैं अच्छा हूँ', translate it to English”
  - “Translate it back”
  - “Now convert it to Bengali”

- 🌐 **Automatic Language Detection**  
  No need to tell it what language you're writing in — Aikya figures it out.

- 🇮🇳 **Supports All Major Indian Languages**  
  Hindi, Tamil, Telugu, Bengali, Malayalam, Kannada, Marathi, Punjabi, Urdu, Assamese, Odia, Gujarati, Bhojpuri, Rajasthani, Maithili, and many more.

- ⚡ **Powered by GPT-4o**  
  Cutting-edge translation using OpenAI’s most capable and fastest model.

- 🛠 **FastAPI + Heroku-Ready**  
  Lightweight backend built with FastAPI — deployable on Heroku, Render, Railway, or any cloud platform.

---

## 🚀 Usage

### ▶️ Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then go to:  
[http://localhost:8000/docs](http://localhost:8000/docs) — Swagger UI to test the `/smart-translate` endpoint.

### 📦 POST Request Format

```
POST /smart-translate
Content-Type: application/json
```

**Body:**
```json
{
  "message": "Translate this to Tamil: I love learning languages."
}
```

---

## 🔐 Environment Setup

Make sure you add your OpenAI API key in a `.env` file:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

And ensure this is loaded in `main.py` using `python-dotenv`.

---

## 📌 Use Cases

- Multilingual customer support bots  
- India-focused health, fintech, or edtech apps  
- Assistive tools for government or NGOs  
- Language accessibility layers for existing products  
- Smart response layer for voice-based agents

---

## 🧑‍💻 Made with ❤️ by [Tripathi Aditya Prakash](https://github.com/tripathiadityaprakash)

---

> “Languages divide us. Aikya unites us — one API at a time.”
