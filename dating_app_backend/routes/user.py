# routes/user.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, UserResponse
from crud import create_user, get_user_by_phone
from database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_phone(db, user.phone_number)
    if db_user:
        raise HTTPException(status_code=400, detail="Số điện thoại đã được đăng ký")
    return create_user(db, user)
