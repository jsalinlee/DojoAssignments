from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "counterKey"
@app.route("/")
def index():
    try:
        session["counter"] += 1
    except:
        session["counter"] = 1
    return render_template("index.html")
@app.route("/counter", methods=["POST"])
def counter():
    if request.form.get("counter") == "Add 2":
        session["counter"] += 1
    elif request.form.get("reset") == "Reset to 1":
        session["counter"] = 0
    return redirect("/")
app.run(debug=True)
