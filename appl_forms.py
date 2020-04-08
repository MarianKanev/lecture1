from flask import Flask, render_template, request

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
       return render_template("index_layout_form.html")

@app.route("/hello", methods=["POST"])
def hello():
        name = request.form.get("username")
        return render_template("hello.html", name=name)
