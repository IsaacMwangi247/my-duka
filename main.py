from flask import Flask, render_template, request, redirect, url_for, flash #first import the Flask object from the flask package
from database import get_products, get_sales, insert_products, insert_sales, available_stock, get_stock, insert_stock, insert_users, check_user_exists


app = Flask(__name__) #create flask application instance with the name app


app.secret_key = '3tbrkiuhngjit66'



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
    flash("Product added successfully", "success")
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
        flash("Insufficient stock", "danger")
        return redirect(url_for('fetch_sales'))
    insert_sales(new_sale)
    flash("Sale completed successfully", "success")
    return redirect(url_for('fetch_sales'))

#getting stock
@app.route('/stocks')
def fetch_stock():
    stocks = get_stock()
    products = get_products()
    return render_template("stocks.html", stocks = stocks, products = products)

#posting stock
@app.route('/add_stock', methods = ['GET', 'POST'])
def add_stock():
    pid = request.form["product_id"]
    quantity = request.form["quantity"]
    new_stock = (pid, quantity)
    insert_stock(new_stock)
    flash("Stock added successfully", "success")
    return redirect(url_for('fetch_stock'))

@app.route('/dashboard')
def dashboard():
    
    return render_template("dashboard.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        registered_user = check_user_exists(email)
        if not registered_user:
            flash('User does not exist, please register', 'danger')
            return redirect(url_for('register'))
        else:
            if password == registered_user[-1]:
                flash('Login successful', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Incorrect password, try again', 'danger')

    return render_template("login.html")


#posting users
@app.route('/register', methods = ['GET',"POST"])
def register():
    if request.method == 'POST':
        full_name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            new_user = (full_name, email, phone_number, password)
            insert_users(new_user)
            flash("User registered successfully", 'success')
            return redirect(url_for('login'))
        else:
            flash("User with this email exists, please login", 'danger')
    return render_template("register.html")


app.run(debug=True)