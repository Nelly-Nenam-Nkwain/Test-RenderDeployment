"""Deployment test"""
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def accueil():
    """landing page"""
    cours = ["Jinja OK", "Static OK", "Render bientôt"]
    return render_template(
        "index.jinja",
        nom="Audrey",
        cours=cours,
        annee=datetime.now().year
    )

@app.route("/ping")
def ping():
    """Testing json"""
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(debug=True)
