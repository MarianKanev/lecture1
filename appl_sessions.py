from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
        if  request.method == "POST":
            note = request.form.get("note")
            notes.append(note)

        return render_template("index_session.html", notes=notes )

