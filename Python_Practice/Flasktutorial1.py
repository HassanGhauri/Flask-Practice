import os
from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv('./.env')

app = Flask(__name__)
app.secret_key = "hello"
URL = os.environ['DB_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)

#required for database running
app.app_context().push()


class users(db.Model):
    _id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
 
 
    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        found_user = users.query.filter_by(name = user).first()
        if found_user:
            session["email"]= found_user.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()


        flash("Logged in successfully")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/user",methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        usr = session["user"]

    
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = usr).first()
            found_user.email = email
            db.session.commit()
            flash("Email saved")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html",email=email)
    else:
        flash("You are not logged in")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        usr = session["user"]
        flash(f"You have successfully logged out {usr}","info")
    session.pop("user",None)
    session.pop("email",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
