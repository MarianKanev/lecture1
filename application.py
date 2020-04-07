from flask import Flask

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
    return "Hello, world!"

# This is called if open 127.0.0.1:500/marian
@app.route("/marian")
def marian():
    return "Hello, Marian!"

# This is called if open 127.0.0.1:500/david
@app.route("/david")
def david():
    return "<h2>Hello, David!</>"