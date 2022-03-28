from flask import render_template, redirect, request, session
from flask_app.models.registration import Registration
from flask_app import app
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    if 'email' in session:
        return redirect('/result/')
    return render_template("index.html")

@app.post('/register')
def register():
    if Registration.is_valid(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        data = {
            "first_name" : request.form['first_name'],
            "last_name" : request.form['last_name'],
            "email" : request.form['email'],
            "gender" : request.form['gender'],
            "confession" : request.form['confession'],
            "password" : pw_hash
        }
        id = Registration.register(data)
        session['email'] = request.form['email']
        return redirect("/result/")
    return redirect('/')

@app.route('/result/')
def result():
    if 'email' not in session:
        return redirect('/')
    data = {
        'email': session['email']
    }
    results = Registration.get_by_email(data)
    print(results)
    return render_template("result.html", results=results)

@app.post('/login')
def login():
    # data = { "email" : request.form["email"] }
    user_in_db = Registration.get_by_email(request.form)

    if not user_in_db:
        flash("Invalid Email/Password",'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email or Password",'login')
        return redirect('/')
    session['email'] = user_in_db.email
    return redirect("/result/")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')




