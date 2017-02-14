from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "floople"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NO_NUMBERS = re.compile(r"^[a-zA-Z'-]+$")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/register", methods=["POST"])
def validation():
    error = None
    if len(request.form["first_name"]) < 1:
        flash("First name can't be blank!")
        error = "error"
    elif not NO_NUMBERS.match(request.form["first_name"]):
        flash("First name can't include numbers or special symbols!")
        error = "error"
    if len(request.form["last_name"]) < 1:
        flash("Last name can't be blank!")
        error = "error"
    elif not NO_NUMBERS.match(request.form["last_name"]):
        flash("Last name can't include numbers or special symbols!")
        error = "error"
    if len(request.form["email"]) < 1:
        flash("Email can't be blank!")
        error = "error"
    elif not EMAIL_REGEX.match(request.form["email"]):
        flash("Invalid Email!")
        error = "error"
    if len(request.form["password"]) < 1:
        flash("Password can't be blank!")
        error = "error"
    if len(request.form["confirm_pass"]) < 1:
        flash("Password confirmation can't be blank!")
        error = "error"
    if request.form["password"] != request.form["confirm_pass"]:
        flash("Passwords don't match!")
        error = "error"
    if error == None:
        flash("Thanks for submitting your information.")
    return redirect("/")
app.run(debug=True)
