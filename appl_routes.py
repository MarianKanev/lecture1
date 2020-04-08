from flask import Flask, render_template

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
       return render_template("index_routes.html")

@app.route("/more")
def more():
       return render_template("more.html")
