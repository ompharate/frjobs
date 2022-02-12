from http.client import HTTPResponse
from flask import *
import requests,sqlite3

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info")
def info():
    return render_template("info.html")




if __name__== "__main__":
    app.run(debug=True)
    
