from fastapi import APIRouter
from starlette import status
from pydantic import BaseModel

from app.persistence.product_repository import (
    fetch_all_products,
    fetch_product_by_id,
    insert_product,
    update_product,
)

router = APIRouter(
    prefix="/products",
    tags=["products"],
)


# https://fastapi.tiangolo.com/tutorial/response-model
class Product(BaseModel):
    id: str | None = None
    code: str
    name: str


@router.get("/", status_code=status.HTTP_200_OK)
def read_products():
    return {"products": fetch_all_products()}


# More info here => https://fastapi.tiangolo.com/tutorial/sql-databases/?h=post#main-fastapi-app
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    return insert_product(code=product.code, name=product.name)


@router.get("/{product_id}", response_model=Product, status_code=status.HTTP_200_OK)
def read_product(product_id: str):
    return {"product": fetch_product_by_id(product_id)}


@router.put("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_product_by_id(product_id: str, product: Product):
    return update_product(code=product.code, name=product.name, product_id=product_id)
