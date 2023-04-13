from flask import Flask, render_template, request
import openai
import os

# setup flask
app = Flask(__name__)

# home route
@app.route("/")
def hello():
    return render_template("index.html")

# preview route
@app.route("/preview", methods=["POST"])
def preview():
    

if __name__ == "__main__":
    app.run(debug=True)