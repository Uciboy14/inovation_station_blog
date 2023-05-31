#!/usr/python3

from flask import Flask, render_template

app = Flask(__name__, static_folder="static", static_url_path="/static")

@app.route("/", strict_slashes=False)
def index():
    return render_template("Index.html")

@app.route("/signIn", strict_slashes=False)
def signIn():
    return render_template("signIn.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
