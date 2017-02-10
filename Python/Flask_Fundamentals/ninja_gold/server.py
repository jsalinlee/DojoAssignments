from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "floople"
@app.route("/")
def index():
    session["gold"] = 0
    return render_template("index.html")
@app.route("/process_money", methods=["post"])
def process():
    if request.form["building"] == "farm":
        session["gold"] += random.randrange(10, 21)
    if request.form["building"] == "cave":
        session["gold"] += random.randrange(5, 11)
    if request.form["building"] == "house":
        session["gold"] += random.randrange(2, 6)
    if request.form["building"] == "casino":
        session["gold"] += random.randrange(-50, 51)
    session["description"] = "You earned " + str(session["gold"]) + " gold!"
    return render_template("index.html")
app.run(debug=True)
