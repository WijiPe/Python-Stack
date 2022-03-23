from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form

counter = 0

@app.route('/')
def index():
    global counter
    if "number" not in session:
        session["number"]=0
        counter += 1
    else: 
        session["number"] += 1
    print(session["number"])
    print(counter)
    return render_template("index.html")

@app.route('/count', methods=['POST'])         
def count():
    counter=request.form['counter']
    session["number"] += int(counter) -1
    return redirect('/')

@app.route('/reset')
def reset():
    session["number"]=0
    return redirect('/')

@app.route('/double')
def double():
    session["number"]+=1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
