from flask import Flask, session, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = "floople"
# Root
@app.route('/')
def index():
    all_users = mysql.query_db("SELECT * FROM users")
    return render_template("index.html", all_users = all_users)
# Login
@app.route('/login', methods=['post'])
def login():
    all_users = mysql.query_db("SELECT * FROM users")
    for i in all_users:
        if i['email'] == request.form['email']:
            if bcrypt.check_password_hash(i['password'], request.form['password']):
                session['id'] = i['id']
                return redirect('/wall')
    flash("Your user info does not match our database.  Please try again.")
    return redirect('/')
# Successful login or registration
@app.route('/wall')
def display_wall():
    if "id" in session:
        query = "SELECT * FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC"
        posted_messages = mysql.query_db(query)
        query = "SELECT * FROM users JOIN comments ON comments.user_id = users.id JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_at;"
        posted_comments = mysql.query_db(query)
        return render_template("wall.html", posted_messages = posted_messages, posted_comments = posted_comments)
    else:
        flash("Please log in to continue.")
        return redirect('/')
# Logout
@app.route('/log_out')
def log_out():
    session.pop('id')
    flash("You have now logged out.  Have a great day!")
    return redirect('/')
# Process registration
@app.route("/process", methods=['post'])
def create_user():
    print "created user"
    error = 0
    # check function for numbers in first/last names
    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)
    # Email validation
    if len(request.form["email"]) == 0:
        flash("Please insert a valid email address.")
        error = 1
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("That email address is invalid.  Please try again.")
        error = 1
    # Check for duplicate emails in database
    else:
        all_users = mysql.query_db("SELECT * FROM users")
        for i in all_users:
            if i['email'] == request.form['email']:
                flash("That email address is already taken.  Please choose a unique email address.")
                error = 1
    # First name validation
    if len(request.form["first_name"]) < 2:
        flash("Please insert your first name.")
        error = 1
    elif hasNumbers(request.form["first_name"]) == True:
        flash("Please remove all numbers from your first name.")
        error = 1
    # Last name validation
    if len(request.form["last_name"]) < 2:
        flash("Please insert your last name.")
        error = 1
    elif hasNumbers(request.form["last_name"]) == True:
        flash("Please remove all numbers from your last name.")
        error = 1
    # Password validation
    if len(request.form["password"]) < 8:
        flash("Please create a password with 8 or more characters.")
        error = 1
    elif (request.form["password"]) != (request.form["confirm"]):
        flash("Please verify that both password fields match.")
        error = 1
    # Successful registration
    if error == 0:
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            "first_name":request.form["first_name"],
            "last_name":request.form["last_name"],
            "email":request.form["email"],
            "password":bcrypt.generate_password_hash(request.form["password"])
        }
        logged_id = mysql.query_db(insert_query, data)
        session['id'] = logged_id
        return redirect("/wall")
    return redirect("/")
@app.route("/postmessage", methods=["post"])
def postmessage():
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    data = {
        "user_id": session["id"],
        "message": request.form["message"]
    }
    print mysql.query_db(query, data)
    return redirect("/wall")
@app.route("/postcomment/<message_id>", methods=["post"])
def postcomment(message_id):

    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    data = {
        "user_id": session["id"],
        "message_id": message_id,
        "comment": request.form["comment"]
    }
    mysql.query_db(query, data)
    return redirect("/wall")
app.run (debug=True)
