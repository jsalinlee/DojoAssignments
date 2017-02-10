from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="floople"
@app.route('/')
def DojoSurvey():
    return render_template("index.html")

@app.route('/users', methods=['post'])
def create_user():
    if len(request.form["name"]) < 1:
        flash("Name cannot be empty!")
        return redirect("/")
    if len(request.form["comment"]) > 120 or len(request.form["comment"]) < 1:
        flash("Comment must be 1-120 characters!")
        return redirect("/")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("results.html", name=name, location=location, language=language, comment=comment)
app.run(debug=True) # run our server
