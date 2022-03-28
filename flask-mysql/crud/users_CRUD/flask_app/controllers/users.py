from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.model_users import User


@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    return render_template("users.html", users = User.get_all())

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    users = User.get_last()
    return redirect(f'/users/show/{users["id"]}')

@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id":id
    }
    users = User.get_one(data)
    print(users)
    return render_template("edit_user.html",users = users)

@app.route("/users/update/<int:id>", methods=['POST'])
def update(id):
    data = {
        "id":id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    print(request.form)
    User.update(data)

    return redirect(f'/users/show/{id}')

@app.route("/users/delete/<int:id>")
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/users/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    users = User.get_one(data)
    return render_template('show.html',users = users)
