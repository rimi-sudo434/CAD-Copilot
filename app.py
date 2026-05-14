from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def get_model():
    try:
        return genai.GenerativeModel("gemini-2.0-flash")
    except:
        try:
            return genai.GenerativeModel("gemini-1.5-flash")
        except:
            return genai.GenerativeModel("gemini-pro")

model = get_model()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_message = request.json.get("message")

        if not API_KEY:
            return jsonify({"reply": "AI service not configured. Please try later."})

        response = model.generate_content(user_message)

        return jsonify({"reply": response.text})

    except:
        return jsonify({"reply": "AI is temporarily unavailable due to quota limit. Please try again later."})