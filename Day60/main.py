from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("htmlforms.html")

@app.route('/login', methods=["POST"])
def get_formdata():
    usr = request.form["username"]
    pwd = request.form["password"]
    return f"<h1> Name: {usr}, Password: {pwd} </h1>"


if __name__ == "__main__":
    app.run(debug=True)

