from flask import Flask, render_template, request, redirect, url_for
#import sqlite3
from flask_sqlalchemy import SQLAlchemy


#SQLAlchemy is defined as an ORM Object Relational Mapping library. This means that it's able to map the relationships in the database into Objects. Fields become Object properties. Tables can be defined as separate Classes and each row of data is a new Object.

#db = sqlite3.connect("books-collection.db")
#cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter1', 'J. K. Rowling', '9.3')")
#db.commit()

app = Flask(__name__)

all_books = []


##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

#created record
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()


#read all records
# all_books = db.session.query(Book).all()

#Read a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()

#Update particular record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

#Update record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

#delete a particular record by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()



@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        # UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

