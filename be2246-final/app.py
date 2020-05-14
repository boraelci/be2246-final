# -*- coding: utf-8 -*-
"""
@author: Bora Elci be2246
Final Project Personal Website
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/1006")
def tenoosix():
    return "This is 1006! Welcome."

#start the server
if __name__ == "__main__":
    app.run()