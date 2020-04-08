from flask import Flask, render_template

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
    text_to_print = "Hello, World - HTML template"
    return render_template("index.html",headline=text_to_print)

# index.html must be in folder templates located in same directory
# where the python script file is located
