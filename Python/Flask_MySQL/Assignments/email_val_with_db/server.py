from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "floople"
mysql = MySQLConnector(app, 'email_validation')
@app.route('/')
def registerEmail():
    return render_template("index.html")
@app.route('/users', methods=['post'])
def submit():
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']):
        flash("Email is not valid!")
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
        "email": request.form["email"]
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM emails"
        emails = mysql.query_db(query)
        return render_template("success.html", data = data, all_emails = emails)
    return redirect("/")
# @app.route("/success", methods=["post"])
app.run(debug=True)
