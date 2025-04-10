# crud.py
from sqlalchemy.orm import Session
from models import User, UserLocation
from schemas import UserCreate
from datetime import datetime
import bcrypt
from geopy.distance import geodesic

# def create_user(db: Session, user: UserCreate):
#     db_user = User(phone_number=user.phone_number, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user_by_phone(db: Session, phone_number: str):
#     return db.query(User).filter(User.phone_number == phone_number).first()


# Đây là phần user
def get_user_by_phone(db: Session, phone_number: str):
    return db.query(User).filter(User.phone_number == phone_number).first()


def create_user(db: Session, phone_number: str, password: str, username: str = None, email: str = None):
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    now = datetime.utcnow().isoformat()

    new_user = User(
        phone_number=phone_number,
        password=hashed_password,
        username=username,
        email=email,
        created_at=now,
        updated_at=now
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



# Đây là phần location
def update_user_location(db: Session, user_id: int, lat: float, lng: float):
    location = db.query(UserLocation).filter_by(user_id=user_id).first()
    if location:
        location.lat = lat
        location.lng = lng
    else:
        location = UserLocation(user_id=user_id, lat=lat, lng=lng)
        db.add(location)
    db.commit()
    db.refresh(location)
    return location


def find_nearby_profiles(db: Session, lat: float, lng: float, radius_km: float):
    users_with_location = (
        db.query(User, UserLocation)
        .join(UserLocation, User.id == UserLocation.user_id)
        .all()
    )

    results = []
    for user, location in users_with_location:
        user_coord = (location.lat, location.lng)
        current_coord = (lat, lng)
        distance_km = geodesic(user_coord, current_coord).km
        if distance_km <= radius_km:
            results.append({
                "id": user.id,
                "name": user.username,
                "avatarUrl": None,  # Gắn avatar nếu có
                "age": None,        # Gắn tuổi nếu có
                "distance": round(distance_km, 2)
            })

    return results









