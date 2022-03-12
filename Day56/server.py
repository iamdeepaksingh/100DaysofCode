# Author: Deepak Kumar Singh
# Descr: Flask project
# Date created: 10/03/2022
# Date Modified: 10/03/2022

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)
