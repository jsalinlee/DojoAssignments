from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "floople"
mysql = MySQLConnector(app, "full_friends")
@app.route("/")
def index():
    query = "SELECT * FROM friends"
    friends= mysql.query_db(query)
    return render_template("index.html", all_friends = friends)
@app.route("/friends", methods=["post"])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    mysql.query_db(query, data)
    return redirect("/")
@app.route("/friends/<id>/edit")
def edit(id):
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    id_tracker = int(id)
    for i in range(len(friends)):
        if friends[i]["id"] == id_tracker:
            friend = friends[i]["first_name"] + " " + friends[i]["last_name"]
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("edit.html", friend=friend, all_friends = friends, id_tracker = id_tracker)
@app.route("/friends/<id>", methods=["post"])
def update(id):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "id": id
    }
    mysql.query_db(query, data)
    return redirect("/")
@app.route("/friends/<id>/delete", methods=["post"])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :delete_id"
    data = {"delete_id": id}
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)
