from flask import Flask, request, jsonify, render_template
from google import genai
import random
import os

app = Flask(__name__)

# =========================================
# 🔑 GET API KEY FROM ENVIRONMENT
# =========================================

API_KEY = os.getenv("GOOGLE_API_KEY")

# =========================================
# 🤖 CREATE GEMINI CLIENT SAFELY
# =========================================

client = None

if API_KEY:
    client = genai.Client(api_key=API_KEY)

# =========================================
# 🌐 HOME PAGE
# =========================================

@app.route("/")
def home():
    return render_template("index.html")

# =========================================
# 💬 AI CHAT ROUTE
# =========================================

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    message = data.get("message").lower()

    try:

        # =========================================
        # ✅ REAL GEMINI API CALL
        # =========================================

        if client:

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=message
            )

            reply = response.text

        else:
            raise Exception("No API Key")

    except Exception:

        # =========================================
        # 🔥 OFFLINE INTELLIGENT FALLBACK
        # =========================================

        if "hello" in message or "hi" in message:

            reply = """
Hello! 👋

I am CAD Copilot AI Assistant.

I can help with:
• Artificial Intelligence
• Programming
• Web Development
• Cyber Security
• Databases
• Computer Networks
• Global Hack Week projects
"""

        elif "global hack week" in message or "ghw" in message:

            reply = """
Global Hack Week (GHW) is an international hackathon event.

Features:
• Project building
• Team collaboration
• Coding challenges
• Workshops
• Innovation
"""

        elif "hackathon" in message:

            reply = """
A hackathon is a collaborative coding competition.

Participants:
• Build software projects
• Solve problems
• Learn technologies
• Present innovations
"""

        elif "cad" in message:

            reply = """
CAD stands for Computer Aided Design.

Applications:
• Engineering drawing
• Architecture
• Mechanical design
• 3D modeling
"""

        elif "copilot" in message:

            reply = """
An AI Copilot assists users intelligently.

Features:
• Smart suggestions
• Automation
• AI assistance
• Productivity improvement
"""

        elif "artificial intelligence" in message or "ai" in message:

            reply = """
Artificial Intelligence enables machines to simulate human intelligence.

Applications:
• Robotics
• Healthcare
• Cyber Security
• Chatbots
• Automation
"""

        elif "machine learning" in message:

            reply = """
Machine Learning is a branch of AI.

Types:
• Supervised Learning
• Unsupervised Learning
• Reinforcement Learning
"""

        elif "deep learning" in message:

            reply = """
Deep Learning uses neural networks with multiple hidden layers.

Applications:
• Image recognition
• Voice assistants
• NLP systems
"""

        elif "python" in message:

            reply = """
Python is a powerful programming language.

Advantages:
• Simple syntax
• AI development
• Web development
• Automation

Popular Libraries:
• Flask
• NumPy
• TensorFlow
"""

        elif "flask" in message:

            reply = """
Flask is a lightweight Python web framework.

Features:
• Fast backend development
• API integration
• Flexible architecture
"""

        elif "html" in message:

            reply = """
HTML structures webpages using elements and tags.
"""

        elif "css" in message:

            reply = """
CSS is used for webpage styling and animations.
"""

        elif "javascript" in message:

            reply = """
JavaScript adds interactivity to websites.
"""

        elif "database" in message:

            reply = """
A database stores and manages digital information.

Examples:
• MySQL
• PostgreSQL
• MongoDB
"""

        elif "sql" in message:

            reply = """
SQL stands for Structured Query Language.
"""

        elif "cloud computing" in message:

            reply = """
Cloud Computing delivers computing resources over the internet.
"""

        elif "cyber security" in message:

            reply = """
Cyber Security protects systems and networks from attacks.
"""

        elif "ethical hacking" in message:

            reply = """
Ethical Hacking identifies security vulnerabilities legally.
"""

        elif "computer network" in message:

            reply = """
Computer Networks connect devices for communication.

Types:
• LAN
• MAN
• WAN
"""

        elif "operating system" in message:

            reply = """
An Operating System manages hardware and software resources.

Examples:
• Windows
• Linux
"""

        elif "linux" in message:

            reply = """
Linux is an open-source operating system widely used in servers.
"""

        elif "windows" in message:

            reply = """
Windows is a graphical operating system developed by Microsoft.
"""

        elif "web development" in message:

            reply = """
Web Development involves creating websites and applications.

Technologies:
• HTML
• CSS
• JavaScript
• Flask
"""

        elif "api" in message:

            reply = """
API stands for Application Programming Interface.

Purpose:
• Connect applications
• Exchange data
"""

        elif "chatbot" in message:

            reply = """
A chatbot simulates human conversation using software.
"""

        elif "internet" in message:

            reply = """
The Internet is a global network connecting millions of devices.
"""

        elif "algorithm" in message:

            reply = """
An algorithm is a step-by-step procedure used to solve problems.
"""

        elif "software engineering" in message:

            reply = """
Software Engineering focuses on designing and maintaining software systems.
"""

        elif "robotics" in message:

            reply = """
Robotics combines engineering and AI to create intelligent machines.
"""

        elif "blockchain" in message:

            reply = """
Blockchain is a decentralized digital ledger technology.
"""

        elif "space" in message:

            reply = """
Space science studies planets, stars, galaxies, and the universe.
"""

        elif "nasa" in message:

            reply = """
NASA is the United States space research agency.
"""

        elif "isro" in message:

            reply = """
ISRO is India's national space research organization.
"""

        elif "project" in message:

            reply = """
This CAD Copilot project demonstrates:

• AI chatbot integration
• Flask backend development
• Gemini API connectivity
• Offline intelligent fallback
• Modern web technologies
"""

        elif "your name" in message:

            reply = """
I am CAD Copilot 🤖

An AI-powered assistant for:
• Technical guidance
• Programming support
• Educational assistance
"""

        else:

            generic_responses = [

                f"CAD Copilot received your question: {message}",

                "Your request was processed successfully.",

                "This is an intelligent offline fallback response.",

                "AI cloud service is temporarily limited, so offline mode is active.",

                "Processing completed successfully."
            ]

            reply = random.choice(generic_responses)

    return jsonify({
        "reply": reply
    })

# =========================================
# 🚀 RUN SERVER
# =========================================

if __name__ == "__main__":
    app.run(debug=True)