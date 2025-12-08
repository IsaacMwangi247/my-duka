from flask import Flask, render_template #first import the Flask object from the flask package
from database import get_products
from database import get_sales

app = Flask(__name__) #create flask application instance with the name app

@app.route('/') # this is a decorator which turns a regular python function into a flask view function, which converts the return value to a http response 
def home():
    return render_template("index.html")

@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html")


@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    return render_template("sales.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

# @app.route('/test/<int:user_id>')
# def test(user_id):
#     return {"id":user_id}

app.run(debug=True)