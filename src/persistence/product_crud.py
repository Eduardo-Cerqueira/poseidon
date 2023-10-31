import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

database_name = os.getenv("DATABASE")
database_port = os.getenv("POSTGRES_PORT")

# Connect to database
conn = psycopg2.connect(
    database=database_name,
    host="localhost",
    user="app",
    password="password",
    port=database_port,
)

cursor = conn.cursor()


def fetch_all_products():
    cursor.execute("SELECT * FROM product")
    return cursor.fetchall()


def fetch_product_by_id(product_id: str):
    cursor.execute("SELECT * FROM product WHERE id = %s", [product_id])
    return cursor.fetchone()


def fetch_product_by_code(code: str):
    cursor.execute("SELECT * FROM product WHERE code = %s", [code])
    return cursor.fetchall()


def fetch_product_by_name(name_id: str):
    cursor.execute("SELECT * FROM product WHERE name = %s", [name_id])
    return cursor.fetchall()


def insert_product(code: str, name: str):
    cursor.execute("INSERT INTO product(code,name) VALUES(%s,%s)", [code, name])
    conn.commit()


def update_product_code(code: str, product_id: str):
    cursor.execute("UPDATE product SET code = %s WHERE id = %s", [code, product_id])
    conn.commit()


def update_product_name(name: str, product_id: str):
    cursor.execute("UPDATE product SET name = %s WHERE id = %s", [name, product_id])
    conn.commit()


def update_product(code: str, name: str, product_id: str):
    cursor.execute(
        "UPDATE product SET code = %s, name = %s WHERE id = %s",
        [code, name, product_id],
    )
    conn.commit()


def delete_product(product_id: str):
    cursor.execute("DELETE FROM product WHERE id = %s", [product_id])
    conn.commit()
