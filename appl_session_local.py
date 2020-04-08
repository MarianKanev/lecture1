from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# As it is define here the notes[] is global variable visible for entire web application
#notes = []

@app.route("/", methods=["GET", "POST"])
def index():
        if session.get("notes") is None:
            session["notes"] = []
        
        if  request.method == "POST":
            note = request.form.get("note")
            session["notes"].append(note)

        return render_template("index_session.html", notes=session["notes"] )

