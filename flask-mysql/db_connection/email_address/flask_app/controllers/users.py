from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.form import Email

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/add/email')         
def add_email():
    if Email.is_valid(request.form) and len(Email.get_duplicate(request.form)) == 0:
        Email.add_email(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    results = Email.get_all()
    return render_template("result.html", results=results)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    Email.delete(data)
    return redirect('/result')
