# routers/signup.py
from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import datetime
import uuid
import re
import bcrypt  # Thư viện băm mật khẩu
from schemas import SignupInput, SignupOutput
from database import SessionLocal
from models import User

router = APIRouter(prefix="/api/auth", tags=["signup"])

# Dependency: lấy session của cơ sở dữ liệu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def validate_password(password: str) -> bool:
    """Kiểm tra mật khẩu có độ dài tối thiểu 8, chứa ít nhất một chữ cái viết hoa và một chữ số."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

@router.post("/register", response_model=SignupOutput, status_code=status.HTTP_201_CREATED)
def register(user: SignupInput, db: Session = Depends(get_db)):
   
    if not user.username or not user.password:
        raise HTTPException(status_code=400, detail="Thiếu username hoặc password")
    
    if not validate_password(user.password):
        raise HTTPException(
            status_code=400,
            detail="Mật khẩu phải có độ dài tối thiểu 8 ký tự, chứa ít nhất một chữ viết hoa và một chữ số"
        )

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username đã tồn tại")
    
    user_id = str(uuid.uuid4())
    created_at = datetime.utcnow()
    code = "CODE-" + user_id[:8]
    
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    
    new_user = User(
        id=user_id,
        username=user.username,
        password=hashed_password,  
        code=code,
        createdAt=created_at
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return SignupOutput(
        id=new_user.id,
        username=new_user.username,
        code=new_user.code,
        message="Tạo tài khoản thành công",
        createdAt=new_user.createdAt
    )
