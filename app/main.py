from fastapi import FastAPI
from app.api.products import router as products_router
from app.api.cart import router as cart_router


app = FastAPI(title="E-Commerce API", version="1.0.0")

app.include_router(products_router)
app.include_router(cart_router)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "E-Commerce API is running"}