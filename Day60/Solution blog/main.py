from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/3dd869df5a6160da62f1").json()
OWN_EMAIL = "thatsme@gmail.com"
OWN_PASSWORD = "1234"
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    print("test1")
    if request.method == 'POST':
        #email = request.form["emailaddress"]
        data = request.form
        print(data["name"])
        print(data["emailaddr"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["emailaddr"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/form-entry', methods=["POST"])
def receive_date():
    print("test")
    email = request.form["emailaddr"]
    return f"<h1> Successfully sent your message.</h1>"


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
