import os
import random
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(route_function):
    """
    If the user is not logged in, redirects to the login page.
    """
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            flash('You need to be logged in to access this page.', 'warning')
            return redirect(url_for('login'))
        return route_function(*args, **kwargs)
    return wrapper


@app.route("/")
@app.route("/index")
def index():
    """
    Returns index page, along with 3 random reviews
    to be displayed.
    """
    reviews = list(mongo.db.reviews.find())
    random.shuffle(reviews)
    selected_reviews = reviews[:3]
    return render_template("index.html", reviews=selected_reviews)

@app.route("/get_reviews")
@login_required
def get_reviews():
    """
    Retrieves all reviews from the database to be displayed
    on the reviews page.
    """
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Add a new instance of user to the database if it doesn't already exist.
    Checks if both password fields match.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        elif request.form.get("password") != request.form.get(
                "password_check"):
            flash("Oops! Passwords do not match.")
            return redirect(url_for("register"))
        else:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            session["user"] = request.form.get("username").lower()
            flash("You have successfully registered!")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Returns the login page and allows user to log in by completing the form.
    Checks the database to ensure the username and password entered match.
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(existing_user["password"],
                                   request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Retrieves username from the session and finds all reviews linked
    to that user. Redirects to the login page if no user is logged in.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        user_reviews = list(mongo.db.reviews.find(
            {"review_by": session["user"]}))
        return render_template(
            "profile.html", username=username, user_reviews=user_reviews)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logs out the session and pops the user. Redirects to login page.
    """
    flash("You are logged out. Bye for now!")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/new_review", methods=["GET", "POST"])
@login_required
def new_review():
    """
    Returns the new_review page and sends the review to the database
    when submitted.
    """
    if request.method == "POST":
        review = {
            "genre_name": request.form.get("genre_name"),
            "song_name": request.form.get("song_name"),
            "artist_name": request.form.get("artist_name"),
            "explicit_language": request.form.get("explicit_language"),
            "review_title": request.form.get("review_title"),
            "review_content": request.form.get("review_content"),
            "review_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Rock on! Your review has been submitted.")
        return redirect(url_for("get_reviews"))

    genres = mongo.db.genres.find().sort("genre_name", 1)
    return render_template("new_review.html", genres=genres)

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)