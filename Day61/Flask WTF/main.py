from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

#One of the biggest reasons why we would choose WTForms over HTML Forms is the built-in validation

# we can inject a header.html and footer.html using Jinja and the code might look something like this:
#
# {% include "header.html" %}
# Web page content
# {% include "footer.html" %}

# Inherited Templates - parent is base.html, child is denied.html
# Super blocks, to override base.html in denied.html

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "password1234"
Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)