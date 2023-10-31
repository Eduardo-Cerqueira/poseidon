from fastapi import FastAPI, HTTPException, status

from persistence.product_repository import fetch_all_products, fetch_product_by_id

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/products", status_code=status.HTTP_200_OK)
def read_products():
    return {"products": fetch_all_products()}


@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
def read_products_id(product_id: str):
    return {"product": fetch_product_by_id(product_id)}


@app.get("/forbidden")
def read_forbidden():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized",
    )


if __name__ == "__main__":
    print("Hello world")
