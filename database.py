import psycopg2

conn = psycopg2.connect(host='localhost',port='5432', user='postgres',password='1234',dbname='my_duka')

cur = conn.cursor()

def get_products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

def insert_products():
    cur.execute("insert into products(name, buying_price, selling_price) values('shoes', 500,900)")
    conn.commit()

product1 = ('milk', 50, 60)
product2 = ('tea', 30, 40)

insert_products(product1)
insert_products(product2)

def insert_sales(values):
    cur.execute(f"insert into sale(pid, quantity) values{values}")
    conn.commit()
sales1 = (2,50)
sales2 = (4,30)
insert_sales(sales1)
insert_sales(sales2)

def get_sales():
    cur.


# import psycopg2

# def insert_two_sales():
#     # Connect to your PostgreSQL database
#     conn = psycopg2.connect(host='localhost',port='5432', user='postgres',password='1234',dbname='my_duka')

#     cur = conn.cursor()

#     # Define the insert query
#     insert_query = sql.SQL("""
#         INSERT INTO sales (pid, quantity)
#         VALUES (%s, %s)
#     """)

#     # Two sales records
#     sales_data = [
#         (2, 50),
#         (5, 60)
#     ]

#     # Execute insert for both records
#     cur.executemany(insert_query, sales_data)

#     # Commit changes
#     conn.commit()
    
#     # Close cursor and connection
#     cur.close()
#     conn.close()

    