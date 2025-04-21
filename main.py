from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os
import re

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# State Memory (in-memory context for demo)
last_input = {"text": None, "from_lang": None, "to_lang": None}

INDIAN_LANGUAGES = [
    "Hindi", "Tamil", "Telugu", "Bengali", "Malayalam",
    "Kannada", "Marathi", "Gujarati", "Punjabi", "Urdu",
    "Assamese", "Odia"
]

class SmartTranslationRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Smart Indian Language Translator is live!"}

@app.post("/smart-translate")
async def smart_translate(request: SmartTranslationRequest):
    user_message = request.message.strip()

    # Memory reference
    global last_input
    detected_target = None
    sentence_to_translate = None

    # Pattern 1: explicit "Translate this to <language>: <text>"
    match_1 = re.search(r"translate.*?to (\w+)[\s:]+(.+)", user_message, re.I)
    if match_1:
        detected_target = match_1.group(1).capitalize()
        sentence_to_translate = match_1.group(2).strip()

    # Pattern 2: "He's saying '<text>', translate it to <language>"
    match_2 = re.search(r"saying ['\"](.+?)['\"].*translate.*to (\w+)", user_message, re.I)
    if match_2:
        sentence_to_translate = match_2.group(1).strip()
        detected_target = match_2.group(2).capitalize()

    # Pattern 3: "Translate it back" → use memory
    if "translate it back" in user_message.lower():
        if last_input["to_lang"] and last_input["text"]:
            sentence_to_translate = last_input["text"]
            detected_target = "English"

    # Pattern 4: "Now translate it to <lang>" or "convert it to <lang>"
    match_4 = re.search(r"(translate|convert).*to (\w+)", user_message, re.I)
    if match_4 and last_input["text"]:
        sentence_to_translate = last_input["text"]
        detected_target = match_4.group(2).capitalize()

    # Pattern 5: "Give this to me in <lang>"
    match_5 = re.search(r"in (\w+)$", user_message.strip().lower())
    if match_5 and last_input["text"]:
        sentence_to_translate = last_input["text"]
        detected_target = match_5.group(1).capitalize()

    if not sentence_to_translate or not detected_target:
        return {
            "error": "Could not understand what to translate or which language to use.",
            "tip": "Try saying something like: 'Translate this to Tamil: I am hungry'"
        }

    if detected_target not in INDIAN_LANGUAGES and detected_target != "English":
        return {"error": f"Unsupported target language: {detected_target}"}

    # Build prompt for GPT
    prompt = (
        f"You are a smart translator. Detect the input language and translate it into {detected_target}. "
        f"Only return the translated sentence. No notes.\n\nText: {sentence_to_translate}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.2
        )
        translated = response.choices[0].message["content"].strip()

        # Save to memory
        last_input["text"] = translated
        last_input["from_lang"] = "auto"
        last_input["to_lang"] = detected_target

        return {
            "translated_text": translated,
            "target_language": detected_target
        }

    except Exception as e:
        return {"error": str(e)}
