from fastapi import FastAPI
from .routers import users

app = FastAPI(title="Lab 3 FastAPI CRUD")

# Підключення роутера, який лежить у папці routers
app.include_router(users.router)

# Це базовий маршрут, щоб при відкритті localhost:8000 щось відображалося
@app.get("/")
def root():
    return {"message": "Welcome to the API. Visit /docs for the Swagger UI."}