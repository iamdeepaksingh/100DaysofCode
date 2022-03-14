# Author: Deepak Kumar Singh
# Descr: Jinja2, serving dynamic content in webpages.
# Date created: 11/03/2022
# Date Modified: 11/03/2022

from flask import Flask, render_template
import requests

# Jinja2
# {% %} used for multiple lines statements, example forloop, if loop, etc.
# {{ }} is used for single line statements.

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/guess/<uname>")
def guess(uname):
    gender_url = f"https://api.genderize.io?name={uname}"
    age_url = f"https://api.agify.io/?name={uname}"
    gender_data = requests.get(gender_url).json()["gender"]
    age_data = requests.get(age_url).json()["age"]

    return render_template("index.html", name=uname, gender=gender_data, age=age_data)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/3dd869df5a6160da62f1"
    blogs = requests.get(blog_url).json()
    return render_template("blog.html", blog_posts=blogs)

@app.route("/blog/all")
def blog():
    blog_url = "https://api.npoint.io/3dd869df5a6160da62f1"
    blogs = requests.get(blog_url).json()
    return render_template("blog.html", blog_posts=blogs)

if __name__== "__main__":
    app.run(debug=True)
