import datetime
from flask import Flask, render_template

app = Flask(__name__)

# This is called if open 127.0.0.1:5000 ( main route)
@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("index_new_year.html",new_year=new_year)
# index.html must be in folder templates located in same directory
# where the python script file is located
