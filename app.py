from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# API KEY from Vercel environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# SAFE MODEL SYSTEM (prevents 404 crash)
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

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "reply": f"Error: {str(e)}"
        })


