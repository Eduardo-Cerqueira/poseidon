from fastapi import FastAPI

from persistence.product_repository import fetch_all_products, fetch_product_by_id

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/products")
def read_products():
    return {"status": 200, "products": fetch_all_products()}


@app.get("/products/{product_id}")
def read_products_id(product_id: str):
    return {"status": 200, "product": fetch_product_by_id(product_id)}


if __name__ == "__main__":
    print("Hello world")
