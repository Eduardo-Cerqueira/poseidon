import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

database_name = os.getenv("DATABASE_NAME")
database_host = os.getenv("DATABASE_HOST")
database_port = os.getenv("POSTGRES_PORT")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")

# Connect to database
conn = psycopg2.connect(
    database=database_name,
    host=database_host,
    user=database_user,
    password=database_password,
    port=database_port,
)

cursor = conn.cursor()


def fetch_all_products() -> [str]:
    """
    Fetch all products information from product table
    :return [str] (String array):
    """
    cursor.execute("SELECT * FROM product")
    return cursor.fetchall()


def fetch_product_by_id(product_id: str) -> [str]:
    """
    Fetch product information using his id (identifier) field to filter from product table
    :parameter product_id:
    :return [str] (String array):
    """
    cursor.execute("SELECT * FROM product WHERE id = %s", [product_id])
    return cursor.fetchone()


def fetch_product_by_code(code: str) -> [str]:
    """
    Fetch product information using his code field to filter from product table
    :parameter code:
    :return [str] (String array):
    """
    cursor.execute("SELECT * FROM product WHERE code = %s", [code])
    return cursor.fetchall()


def fetch_product_by_name(name: str) -> [str]:
    """
    Fetch product information using his name field to filter from product table
    :parameter name:
    :return [str] (String array):
    """
    cursor.execute("SELECT * FROM product WHERE name = %s", [name])
    return cursor.fetchall()


def insert_product(code: str, name: str) -> None:
    """
    Insert product into product table
    :parameter name:
    :parameter code:
    """
    cursor.execute("INSERT INTO product(code,name) VALUES(%s,%s)", [code, name])
    conn.commit()


def update_product_code(code: str, product_id: str) -> None:
    """
    Update product code field using his id field to filter from product table
    :parameter code:
    :parameter product_id:
    """
    cursor.execute("UPDATE product SET code = %s WHERE id = %s", [code, product_id])
    conn.commit()


def update_product_name(name: str, product_id: str) -> None:
    """
    Update product name field using his id field to filter from product table
    :parameter name:
    :parameter product_id:
    """
    cursor.execute("UPDATE product SET name = %s WHERE id = %s", [name, product_id])
    conn.commit()


def update_product(code: str, name: str, product_id: str) -> None:
    """
    Update all product fields using his id field to filter from product table
    :parameter code:
    :parameter name:
    :parameter product_id:
    """
    cursor.execute(
        "UPDATE product SET code = %s, name = %s WHERE id = %s",
        [code, name, product_id],
    )
    conn.commit()


def delete_product(product_id: str) -> None:
    """
    Delete product using his id field to filter from product table
    :parameter product_id:
    """
    cursor.execute("DELETE FROM product WHERE id = %s", [product_id])
    conn.commit()
