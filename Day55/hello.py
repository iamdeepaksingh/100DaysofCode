from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrap_function():
        return "<b>" + function() + "</b>"
    return wrap_function

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
@make_bold
@make_underlined
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"

@app.route("/user/<path:name>")
def greet(name):
    return f"Hello there {name}"

if __name__ == "__main__":
    app.run()
    
