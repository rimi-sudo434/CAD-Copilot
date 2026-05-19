from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_message = request.json.get("message")

        if not API_KEY:
            return jsonify({
                "reply": "AI service is not configured yet."
            })

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except:
        return jsonify({
            "reply": "AI is temporarily unavailable due to quota limits. Please try again later."
        })
