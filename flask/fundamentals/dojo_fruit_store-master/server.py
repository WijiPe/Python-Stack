from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    firstName=request.form['first_name']
    lastname=request.form['last_name']
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    print(f"Charging {firstName} {lastname} for {int(strawberry)+int(raspberry)+int(apple)} fruits")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    