from flask import Flask, render_template, request, redirect, url_for #first import the Flask object from the flask package
from database import get_products, get_sales, insert_products, insert_sales, available_stock, get_stock, insert_stock


app = Flask(__name__) #create flask application instance with the name app

@app.route('/') # this is a decorator which turns a regular python function into a flask view function, which converts the return value to a http response 
def home():
    return render_template("index.html")


#getting products
@app.route('/products')
def fetch_products():
    products = get_products()
    return render_template("products.html", products = products)

#posting products
@app.route('/add_products', methods = ['GET', 'POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]
    new_product = (product_name, buying_price, selling_price)
    insert_products(new_product)
    return redirect(url_for('fetch_products'))

# getting sales
@app.route('/sales')
def fetch_sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html", sales = sales, products = products)


#posting sales
@app.route('/add_sale', methods = ['GET', 'POST'])
def add_sale():
    pid = request.form["pid"]
    quantity = request.form["quantity"]
    new_sale = (pid, quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        print("Insufficient stock")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    return redirect(url_for('fetch_sales'))

#getting stock
@app.route('/stocks')
def fetch_stock():
    stock = get_stock()
    products = get_products()
    return render_template("stocks.html", stock = stock, products = products)

#posting stock
@app.route('/add_stock', methods = ['GET', 'POST'])
def add_stock():
    pid = request.form["product_id"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        print("Insufficient stock")
        return redirect(url_for('fetch_stock'))
    insert_stock(new_stock)
    return redirect(url_for('fetch_stock'))



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