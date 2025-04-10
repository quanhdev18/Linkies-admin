# main.py
from fastapi import FastAPI
from database import engine, Base
import models  # Import model để tạo bảng
from routes import user, auth, chat, signup, location

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Dating App API",
    description="API cho dự án Dating App",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Dating App API!"}

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(signup.router)
app.include_router(location.router)