from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])         
def result():
    yourName=request.form['your_name']
    session['yourName']=yourName
    yourPet=request.form['pet']
    session['yourPet']=yourPet
    fav=request.form['fav']
    session['fav']=fav
    comment=request.form['comment']
    session['comment']=comment
    if 'choice' not in request.form:
        choice = '...'
    else:
        choice=request.form['choice']
    session['choice']=choice
    if request.form.get('confession') == None:
        confession = '...'
    else:
        confession=request.form.get('confession')
    session['confession']=confession
    return render_template("result.html",yourName=yourName, yourPet=yourPet, fav=fav, comment=comment, choice=choice, confession=confession)
    
if __name__ == "__main__":
    app.run(debug=True)