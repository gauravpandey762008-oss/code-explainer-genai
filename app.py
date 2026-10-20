from flask import Flask, render_template, request, jsonify
from ai import ask_ai

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="💻 AI Code Explainer",
                           hint="Koi bhi code paste karo...")

@app.route("/run", methods=["POST"])
def run():
    code = request.json["text"]
    prompt = ("Tum ek teacher ho. Is code ko beginner ko Hinglish me line-by-line samjhao, "
              "phir batao isme koi bug ya improvement ho sakta hai kya.\n\n" + code)
    return jsonify(result=ask_ai(prompt))

app.run(debug=True)
