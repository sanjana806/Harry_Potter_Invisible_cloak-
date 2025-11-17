# --------------------------------------------
# Science & Technology Project: Harry Potter Invisible Cloak
# By Team Sanjana, Isha & Trisha
# Mentor: Devashish Kumar
# Flask App + Animated UI + Run Button
# --------------------------------------------

from flask import Flask, render_template_string
import subprocess
import threading

app = Flask(__name__)

# --------------------------------------------
# FUNCTION TO RUN INVISIBLE CLOAK PROJECT
# --------------------------------------------
def run_invisible_cloak():
    # This runs your invisible_cloak.py file
    subprocess.run(["python", "invisible_cloak.py"])

# --------------------------------------------
# HTML PAGE (Animated Interface)
# --------------------------------------------
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Harry Potter Invisible Cloak</title>
    <style>
        body {
            margin: 0;
            font-family: 'Poppins', sans-serif;
            color: white;
            text-align: center;
            background: linear-gradient(-45deg, #0b0c10, #1e1e2f, #2e2e4f, #0b0c10);
            background-size: 400% 400%;
            animation: gradientShift 10s ease infinite;
        }

        @keyframes gradientShift {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        header {
            padding: 60px 20px;
            background: linear-gradient(90deg, #5f27cd, #341f97);
            box-shadow: 0px 3px 15px #5f27cd;
        }
        header h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.1rem;
            color: #dcdde1;
        }

        .project-section {
            margin-top: 60px;
            padding: 30px;
        }

        .project-card {
            background-color: rgba(30, 30, 47, 0.9);
            padding: 40px;
            border-radius: 20px;
            width: 80%;
            max-width: 700px;
            margin: auto;
            box-shadow: 0 0 20px #5f27cd;
            transition: 0.4s;
        }
        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 0 30px #00d2d3;
        }

        button {
            margin-top: 20px;
            background-color: #00d2d3;
            color: black;
            padding: 12px 30px;
            border: none;
            border-radius: 12px;
            font-size: 1.1rem;
            cursor: pointer;
            transition: 0.3s;
        }
        button:hover {
            background-color: #01a3a4;
            color: white;
            transform: scale(1.1);
            box-shadow: 0 0 20px #00d2d3;
        }

        footer {
            margin-top: 80px;
            background: #1e1e2f;
            padding: 20px;
            color: #aaa;
            font-size: 0.9rem;
            box-shadow: 0 -3px 15px #5f27cd;
        }
    </style>
</head>
<body>
    <header>
        <h1>Harry Potter Invisible Cloak</h1>
        <p>Science & Technology Fair 2025 | By Team Sanjana, Isha & Trisha</p>
    </header>

    <section class="project-section">
        <div class="project-card">
            <h2>Become Invisible Using AI & Computer Vision</h2>
            <p>Inspired by Harry Potter's magical cloak, this project uses OpenCV to make a specific-colored cloak disappear in real-time using webcam detection and background subtraction.</p>

            <form action="/run_invisible_cloak" method="post">
                <button type="submit">🪄 Launch Invisible Cloak</button>
            </form>
        </div>
    </section>

    <footer>
        Guided by Mentor: Devashish Kumar | Team Sanjana, Isha & Trisha | Powered by Flask + OpenCV
    </footer>
</body>
</html>
"""

# --------------------------------------------
# ROUTES
# --------------------------------------------
@app.route("/")
def home():
    return render_template_string(html_code)

@app.route("/run_invisible_cloak", methods=["POST"])
def run_invisible_cloak_route():
    threading.Thread(target=run_invisible_cloak).start()
    return "<h2>🪄 Launching Invisible Cloak...<br><a href='/'>⬅ Go Back</a></h2>"

# --------------------------------------------
# MAIN
# --------------------------------------------
if __name__ == "__main__":
    print("🚀 Invisible Cloak UI running at: http://127.0.0.1:5000")
    app.run(debug=True)
