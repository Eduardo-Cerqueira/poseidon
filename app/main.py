from fastapi import FastAPI, HTTPException, status
from app.routers import products

app = FastAPI()
app.include_router(products.router)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/forbidden")
def read_forbidden():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You are not authorized",
    )


if __name__ == "__main__":
    print("Hello world")
