import psycopg2

conn = psycopg2.connect(host='localhost',port='5432', user='postgres',password='1234',dbname='my_duka')

cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products 

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price,selling_price) values{values}")
    conn.commit()


def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

#method 1 using f string
def insert_sales(values):
    cur.execute(f"insert into sales(pid, quantity)values{values}")
    conn.commit()

#method 2 - using placeholders
def insert_sales_2(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

def available_stock(pid):
    cur.execute(f"select sum(stock_quantity) from stock where pid = {pid}")
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f"select sum(quantity) from sales where pid = {pid}")
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales

def get_stock():
    cur.execute("select * from stock")
    stock = cur.fetchall()
    return stock

def insert_stock(values):
    cur.execute(f"insert into stock(pid, stock_quantity)values{values}")
    conn.commit()


def insert_users(values):
    cur.execute(f"insert into users(full_name, email, phone_number, password)values{values}")
    conn.commit()

def check_user_exists(email):
    cur.execute("select * from users where email = %s", (email,))
    user = cur.fetchone()
    return user

# sales per product
def get_salesperproduct():
    cur.execute("SELECT p.id, p.name, SUM(s.quantity * p.selling_price) AS total_sales FROM products p JOIN sales s ON p.id = s.pid GROUP BY p.id, p.name ORDER BY total_sales DESC;")
    salesperproduct = cur.fetchall()
    return salesperproduct

# sales per day
def get_salesperday():
    cur.execute("SELECT DATE(s.created_at) AS sale_date, SUM(s.quantity * p.selling_price) AS total_sales FROM sales s JOIN products p ON s.pid = p.id GROUP BY DATE(s.created_at) ORDER BY sale_date;")
    salesperday = cur.fetchall()
    return salesperday

# profit per day
def get_profitsperday():
    cur.execute("SELECT DATE(s.created_at) AS sale_date, SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit FROM sales s JOIN products p ON s.pid = p.id GROUP BY DATE(s.created_at) ORDER BY sale_date;")
    profit_perday = cur.fetchall()
    return profit_perday

# profit per product
def get_profitsperday():
    cur.execute("SELECT p.id, p.name, SUM((p.selling_price - p.buying_price) * s.quantity) AS total_profit FROM products p JOIN sales s ON p.id = s.pid GROUP BY p.id, p.name ORDER BY total_profit DESC;")
    profit_perday = cur.fetchall()
    return profit_perday




