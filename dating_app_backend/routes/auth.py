# routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse
from crud import get_user_by_phone
from database import SessionLocal

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_phone(db, user.phone_number)
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Thông tin đăng nhập không chính xác")
    # Ở đây bạn có thể tạo token JWT hoặc trả về thông tin người dùng
    return {"message": "Đăng nhập thành công", "user": {"id": db_user.id, "phone_number": db_user.phone_number}}
