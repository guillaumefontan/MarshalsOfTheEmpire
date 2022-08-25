import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)

#Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")

#Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

class Page:
    title = ""
    info = ""
    action = ""
    buttonText = ""
    options = []

class Option:
    def __init__(self, name, value):
        self.name = name
        self.value = value


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("/age")

    else:
        Page.info = "Click 'Find out' to begin the quiz"
        Page.action = "/"
        Page.buttonText = "Find out"
        Page.options.clear()

        return render_template("index.html", page=Page)


@app.route("/age", methods=["GET", "POST"])
def age():
    if request.method == "POST":
        session["age"] = request.form.get("MarshalsQuiz")
        return redirect("/socioeconomics")

    else:
        Page.title = "1/6"
        Page.info = "What is your age range?"
        Page.action = "/age"
        Page.buttonText = "Next"

        Page.options.append(Option("0-34", 1))
        Page.options.append(Option("35-39", 2))
        Page.options.append(Option("40-44", 3))
        Page.options.append(Option("45-49", 4))
        Page.options.append(Option("50+", 5))

        return render_template("index.html", page=Page)


@app.route("/socioeconomics", methods=["GET", "POST"])
def socioeconomics():
    if request.method == "POST":
        session["socioeconomic_background"] = request.form.get("MarshalsQuiz")
        return redirect("/geography")

    else:
        Page.title = "2/6"
        Page.info = "What is your socio-economic background?"
        Page.action = "/socioeconomics"
        Page.buttonText = "Next"

        Page.options.clear()
        Page.options.append(Option("Lower class", 1))
        Page.options.append(Option("Middle class", 2))
        Page.options.append(Option("Upper class", 3))

        return render_template("index.html", page=Page)


@app.route("/geography", methods=["GET", "POST"])
def geography():
    if request.method == "POST":
        session["geographic_background"] = request.form.get("MarshalsQuiz")
        return redirect("/adoption")

    else:
        Page.title = "3/6"
        Page.info = "Where were you born?"
        Page.action = "/geography"
        Page.buttonText = "Next"

        Page.options.clear()
        Page.options.append(Option("Countryside", 1))
        Page.options.append(Option("Mountains", 2))
        Page.options.append(Option("Rural coastline", 3))
        Page.options.append(Option("Urban area", 4))
        Page.options.append(Option("Large city", 5))

        return render_template("index.html", page=Page)


@app.route("/adoption", methods=["GET", "POST"])
def adoption():
    if request.method == "POST":
        session["adoption_speed"] = request.form.get("MarshalsQuiz")
        return redirect("/leadership")

    else:
        Page.title = "4/6"
        Page.info = "A new product is released. It has the potential to greatly improve your life, but could also have disastrous consequences. How quick are you to adopt it?"
        Page.action = "/adoption"
        Page.buttonText = "Next"

        Page.options.clear()
        Page.options.append(Option("You set up camp outside the store", 1))
        Page.options.append(Option("You wait for reviews before making up your mind", 2))
        Page.options.append(Option("You wait for the product to mature", 3))

        return render_template("index.html", page=Page)


@app.route("/leadership", methods=["GET", "POST"])
def leadership():
    if request.method == "POST":
        session["leadership"] = request.form.get("MarshalsQuiz")
        return redirect("/death")

    else:
        Page.title = "5/6"
        Page.info = "What kind of a leader are you?"
        Page.action = "/leadership"
        Page.buttonText = "Next"

        Page.options.clear()
        Page.options.append(Option("A tough, authoritarian leader who values discipline", 1))
        Page.options.append(Option("A brave, charismatic leader who relies on instinct", 2))
        Page.options.append(Option("A workaholic, you preach preparation and administration", 3))

        return render_template("index.html", page=Page)


@app.route("/death", methods=["GET", "POST"])
def death():
    if request.method == "POST":
        session["death"] = request.form.get("MarshalsQuiz")
        return redirect("/results")

    else:
        Page.title = "6/6"
        Page.info = "How do you envision your death?"
        Page.action = "/death"
        Page.buttonText = "Results"

        Page.options.clear()
        Page.options.append(Option("Dying in the heat of the action, doing what you love", 1))
        Page.options.append(Option("Passing away peacefully surrounded by your loved ones", 2))
        Page.options.append(Option("Rotting away, contemplating your regrets", 3))

        return render_template("index.html", page=Page)


@app.route("/results")
def results():
    relatedMarshals = []
    fields = ["age", "socioeconomic_background", "geographic_background", "adoption_speed", "leadership", "death"]

    for field in fields:
        value = session[field]
        query = f"SELECT marshals.id FROM marshals, specs where marshals.spec_id = specs.id and {field} = {value};"
        marshalsSQL = db.execute(query)
        for marshal in marshalsSQL:
            relatedMarshals.append(marshal['id'])

    idCount = []
    idSet = set(relatedMarshals)

    for id in idSet:
        idCount.append(relatedMarshals.count(id))

    matchId = relatedMarshals[idCount.index(max(idCount))]
    result = db.execute("SELECT name, description, image FROM marshals where id = (?);", matchId)[0]
    return render_template("result.html", marshal=result)
