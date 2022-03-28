from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return redirect('/authors')

@app.route("/authors")
def author():
    authors = Author.get_all()
    return render_template("authors.html", authors = authors)

@app.post('/authors/create')
def create_author():
    Author.save(request.form)
    return redirect('/authors')


@app.route("/authors/<int:id>")
def show(id):
    data = {
        "id":id
    }
    books = Book.get_book_in_author(data)
    get_books = Book.get_unfav_book(data)
    return render_template("author_show.html", books = books, get_books = get_books)

@app.post("/authors/<int:author_id>")
def add_book(author_id):
    data = {
        "author_id":author_id,
        "book_id":request.form['get_book.id']
    }
    Book.add_book_favorite(data)
    return redirect(f"/authors/{author_id}")

@app.route("/books")
def book():
    books = Book.get_all()
    return render_template("books.html", books = books)

@app.post('/books/create')
def create_book():
    Book.save(request.form)
    return redirect('/books')

@app.route("/books/<int:id>")
def book_show(id):
    data = {
        "id":id
    }
    book_ids = Author.get_author_in_book(data)
    authors = Book.get_unfav_author(data)
    return render_template ("book_show.html", book_ids=book_ids, authors=authors)

@app.post("/books/<int:book_id>")
def add_author(book_id):
    data = {
        "book_id":book_id,
        "author_id":request.form['author_id']
    }
    Book.add_book_favorite(data)
    return redirect(f"/books/{book_id}")



# @app.route('/users/new')
# def new():
#     return render_template("new_user.html")

# @app.route("/user/edit/<int:id>")
# def edit(id):
#     data = {
#         "id":id
#     }
#     users = User.get_one(data)
#     print(users)
#     return render_template("edit_user.html",users = users)

# @app.route("/users/update/<int:id>", methods=['POST'])
# def update(id):
#     data = {
#         "id":id,
#         "first_name": request.form['first_name'],
#         "last_name": request.form['last_name'],
#         "email": request.form['email']
#     }
#     print(request.form)
#     User.update(data)

#     return redirect(f'/users/show/{id}')

# @app.route("/users/delete/<int:id>")
# def delete(id):
#     data = {
#         "id":id
#     }
#     User.delete(data)
#     return redirect('/users')

# @app.route('/users/show/<int:id>')
# def show(id):
#     data = {
#         "id":id
#     }
#     users = User.get_one(data)
#     return render_template('show.html',users = users)
