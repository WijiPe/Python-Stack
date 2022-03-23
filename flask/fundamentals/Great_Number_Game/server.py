from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

winner_info = {}

@app.route('/')
def index():
    result_num = random.randint(1,2)
    session["result_num"] = result_num
    session["num"] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def result():
    result_num=session["result_num"]
    num=request.form['num']
    session["num"]+=1
    if session["num"] > 4:
        return render_template("lose.html")
    if int(num) > result_num:
        return render_template("guess.html", wrong_num=f"Too High!")
    if int(num) < result_num:
        return render_template("guess.html", wrong_num=f"Too Low!")
    if int(num) == result_num:
        return render_template("result.html", right_num=int(num))

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    yourName=request.form['your_name']
    session['yourName']=yourName
    score=session["num"]
    winner_info [yourName]=score
    return render_template("leaderboard.html", score=score, yourName=yourName,winner_info=winner_info)

@app.route('/form', methods=['GET'])
def form():
    return render_template("form.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)