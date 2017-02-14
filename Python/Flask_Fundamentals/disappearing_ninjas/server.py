from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/<ninja>")
def ninja(ninja):
    return render_template("index.html", ninja=ninja)
@app.route("/ninja/<ninja_color>")
def show_ninja(ninja_color):
    return render_template("ninja.html", ninja_color=ninja_color)
app.run(debug=True)
