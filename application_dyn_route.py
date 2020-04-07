from flask import Flask

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
    return "Hello, world!"

# This is called if open 127.0.0.1:5000/any name
@app.route("/<string:name>")
def hello(name):
    return f"Hello, {name}!"
