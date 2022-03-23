from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index(num1=4, num2=4):
    return render_template("index.html", num1=num1, num2=num2)

@app.route("/4")
def style1(num1=4, num2=8):
    return render_template("index.html", num1=num1, num2=num2)

@app.route("/<int:num1>/<int:num2>")
def style2(num1, num2):
    return render_template("index.html", num1=num1, num2=num2)

@app.route("/<int:num1>/<int:num2>/<string:color1>/<string:color2>")
def style3(num1, num2, color1, color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)


if __name__ == '__main__':
    app.run(port=5000,debug=True)