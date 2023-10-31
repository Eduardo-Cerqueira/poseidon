import psycopg2

# Connect to the database
conn = psycopg2.connect(database="poseidon",
                        host="localhost",
                        user="app",
                        password="password",
                        port="5432")

# Create a cursor for database operations
cur = conn.cursor()

# SELECT all orders from the "order" table
def get_all_order():
    cur.execute("SELECT * FROM public.order;")
    return cur.fetchall()


# SELECT an order by its ID
def get_order_by_id(id):
    cur.execute("SELECT * FROM public.order WHERE id = %s", (id,))
    return cur.fetchall()

# SELECT orders by customer name
def get_order_by_customer(customer):
    cur.execute("SELECT * FROM public.order WHERE customer = %s", (customer,))
    return cur.fetchall()

# INSERT a new order into the "order" table
def insert_into_order(customer, product, quantity):
    cur.execute("INSERT INTO public.order (customer, product, quantity) VALUES (%s, %s, %s)", (customer, product, quantity))
    conn.commit()

# UPDATE an order by its ID
def update_customer_family(id, customer, product, quantity):
    cur.execute("UPDATE public.order SET customer = %s, product = %s, quantity = %s WHERE id = %s", (customer, product, quantity, id))
    conn.commit()

# DELETE an order by its ID
def delete_order(id):
    cur.execute("DELETE FROM public.order WHERE id = %s", (id))
    conn.commit()

# Call the get_all_order function to retrieve and print data
get_all_order()

# Close the cursor and the database connection
cur.close()
conn.close()
