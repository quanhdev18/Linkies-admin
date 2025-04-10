# routers/signin.py
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import bcrypt  # Thư viện băm mật khẩu
from schemas import SigninInput, SigninOutput
from database import SessionLocal
from models import User

router = APIRouter(prefix="/api/auth", tags=["signin"])

# Dependency: lấy session của cơ sở dữ liệu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signin", response_model=SigninOutput)
def signin(user: SigninInput, db: Session = Depends(get_db)):
    # Tìm kiếm user trong CSDL
    existing_user = db.query(User).filter(User.username == user.username).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Username không tồn tại")
    
    # Kiểm tra mật khẩu bằng cách so sánh với mật khẩu đã băm
    if not bcrypt.checkpw(user.password.encode("utf-8"), existing_user.password.encode("utf-8")):
        raise HTTPException(status_code=400, detail="Mật khẩu không đúng")
    
    # Giả lập tạo token (nên dùng JWT để tạo token thực tế)
    token = f"dummy-token-{existing_user.id}"
    expire_in = "3600"  # Token sống 3600 giây (1 giờ)
    
    return SigninOutput(token=token, expireIn=expire_in)
