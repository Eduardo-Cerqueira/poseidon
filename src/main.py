from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from persistence.product_repository import (
    fetch_all_products,
    fetch_product_by_id,
    insert_product,
    update_product,
)

app = FastAPI()


# https://fastapi.tiangolo.com/tutorial/response-model
class Product(BaseModel):
    id: str | None = None
    code: str
    name: str


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/products", status_code=status.HTTP_200_OK)
def read_products():
    return {"products": fetch_all_products()}


@app.get(
    "/products/{product_id}", response_model=Product, status_code=status.HTTP_200_OK
)
def read_product(product_id: str):
    return {"product": fetch_product_by_id(product_id)}


@app.put("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_product_by_id(product_id: str, product: Product):
    return update_product(code=product.code, name=product.name, product_id=product_id)


@app.get("/forbidden")
def read_forbidden():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized",
    )


# More info here => https://fastapi.tiangolo.com/tutorial/sql-databases/?h=post#main-fastapi-app
@app.post("/products/", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    return insert_product(code=product.code, name=product.name)


if __name__ == "__main__":
    print("Hello world")
