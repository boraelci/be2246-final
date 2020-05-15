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
def main():
    return render_template("index.html")

@app.route("/1006")
def tenoosix():
    return "This is 1006! Welcome."

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

#start the server
if __name__ == "__main__":
    app.run()