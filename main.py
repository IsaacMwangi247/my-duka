from flask import Flask, render_template, request, redirect, url_for, flash, session #first import the Flask object from the flask package
from database import get_products, get_sales, insert_products, insert_sales, available_stock, get_stock, insert_stock, insert_users, check_user_exists, sales_per_day, sales_per_product, profit_per_day, profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__) #create flask application instance with the name app

bcrypt = Bcrypt(app)

# secret key that signs session data
app.secret_key = '3tbrkiuhngjit66'


# Index route
@app.route('/') # this is a decorator which turns a regular python function into a flask view function, which converts the return value to a http response 
def home():
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def protected(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return protected


#getting products
@app.route('/products')
@login_required
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
@login_required
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
@login_required
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
@login_required
def dashboard():
    product_sales = sales_per_product()
    daily_sales = sales_per_day()
    product_profit = profit_per_product()
    daily_profit = profit_per_day()

    product_names = [i[0] for i in product_sales] 
    sales_per_p = [float(i[1]) for i in product_sales]
    profit_per_p = [float(i[1]) for i in product_profit]

    date = [str(i[0]) for i in daily_profit]
    sales_per_d = [float(i[0]) for i in daily_sales]
    profit_per_d = [float(i[1]) for i in daily_profit]

    return render_template("dashboard.html",
                           product_names=product_names, sales_per_p=sales_per_p, profit_per_p=profit_per_p, profit_per_d=profit_per_d, sales_per_d=sales_per_d, date=date)



@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash('User does not exist, please register', 'danger')
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1], password):
                flash('Login successful', 'success')
                session['email'] = email
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
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name, email, phone_number, hashed_password)
            insert_users(new_user)
            flash("User registered successfully", 'success')
            return redirect(url_for('login'))
        else:
            flash("User with this email exists, please login", 'danger')
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("Logged out successfully",'success')
    return redirect(url_for('login'))


app.run(debug=True)