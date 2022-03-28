from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.form import Form

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/add/form')         
def add_info():
    if Form.is_valid(request.form):
        Form.add_info(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    results = Form.get_last()
    return render_template("result.html", results=results)
