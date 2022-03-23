from flask import Flask

app = Flask(__name__)


@app.route("/")
def landingPage():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/john')
def greeting_john():
    return 'Hi John!'

@app.route('/say/jay')
def greeting_jay():
    return 'Hi Jay!'

@app.route('/say/<name>')
def greeting_name(name):
    return f"Hi {name}!"

@app.route("/repeat/<int:num>/<string:word>")
def greeting(num, word):
    return f"{word*num}"


if __name__ == '__main__':
    app.run(port=5000,debug=True)
