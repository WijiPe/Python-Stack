from flask import render_template, redirect, request, session
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)


@app.route('/result')
def result():
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': session['id']
    }
    users = User.get_by_id(data)
    cars = Car.get_cars_show_owner()
    return render_template("dashboard.html", users=users, cars=cars)

@app.route("/to_add")
def to_add_car():
    if 'id' not in session:
        return redirect('/')
    return render_template ("add_car.html")

@app.post('/add')
def add_car():
    if 'id' not in session:
        return redirect('/')
    if Car.is_valid(request.form):
        data = {
            'user_id': session['id'],
            **request.form
        }
        Car.add_car(data)
        return redirect("/result")
    return redirect('/to_add')

@app.route("/to_edit/<int:id>")
def to_edit_car(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    cars = Car.get_one_car(data)
    if cars.user_id == session['id']:
        return render_template("edit_car.html", cars=cars)
    return redirect('/')

@app.post('/edit/<int:id>')
def edit_car(id):
    if 'id' not in session:
        return redirect('/')
    if Car.is_valid(request.form):
        data = {
            'id': id,
            'model': request.form['model'],
            'make': request.form['make'],
            'price': request.form['price'],
            'description': request.form['description'],
            'year': request.form['year'],
        }
        Car.edit_car(data)
        return redirect("/result")
    return redirect(f'/to_edit/{id}')

@app.route('/delete/car/<int:id>')
def delete_car(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': id,
    }
    cars = Car.get_one_car(data)
    if cars.user_id == session['id']:
        Car.delete_car(data)
        return redirect("/result")
    return redirect('/')

@app.route("/to_show/<int:id>")
def to_show(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "id":id
    }
    data2 = {
        "id": session['id']
    }
    cars = Car.get_one_car_show_owner(data)
    results = User.get_by_id(data2)
    return render_template("cars.html", cars = cars, results = results)

@app.route('/purchase/car/<int:id>')
def purchase_car(id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "id":id,
        "user_id":session['id']
    }
    cars = Car.purchase_car(data)
    # return redirect('/result')
    return redirect('/show_result')


@app.route('/show_result')
def show_result():
    if 'id' not in session:
        return redirect('/')
    data = {
        'id': session['id']
    }
    users = User.get_by_id(data)
    cars = Car.get_last()
    return render_template("owner_car.html", users=users, cars=cars)

