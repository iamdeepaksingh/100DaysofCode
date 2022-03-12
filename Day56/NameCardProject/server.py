# Author: Deepak Kumar Singh
# Descr: Name card project using Flask.
# Date created: 11/03/2022
# Date Modified: 11/03/2022

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)
