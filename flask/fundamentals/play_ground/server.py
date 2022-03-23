from flask import Flask, render_template


app = Flask(__name__)

@app.route("/play")
def index():
    return render_template('index.html', times=3)

@app.route("/play/<int:num>/<color>")
def play(num, color):
    return render_template('index.html', num=num , color=color)

if __name__ == '__main__':
    app.run(port=5000,debug=True)