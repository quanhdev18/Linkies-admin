from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import UpdateLocationInput, UpdateLocationOutput, NearbySearchInput, NearbySearchOutput, ProfileInfo
from crud import update_user_location, find_nearby_profiles


router = APIRouter(prefix="/api/profiles", tags=["location"])


# 🔐 Giả lập xác thực bằng token
def get_current_user_id(authorization: str = Header(...)) -> int:
    if not authorization.startswith("Bearer dummy-token-"):
        raise HTTPException(status_code=401, detail="Token không hợp lệ")
    try:
        return int(authorization.split("-")[-1])
    except:
        raise HTTPException(status_code=401, detail="Không lấy được userId")


@router.put("/location", response_model=UpdateLocationOutput)
def update_location(input: UpdateLocationInput, db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    update_user_location(db, user_id, input.lat, input.lng)
    return {
        "code": "SUCCESS",
        "message": "Cập nhật vị trí thành công"
    }


@router.get("/nearby", response_model=NearbySearchOutput)
def find_profiles_nearby(input: NearbySearchInput = Depends(), db: Session = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    profiles = find_nearby_profiles(db, input.lat, input.lng, input.radius)
    return {
        "code": "SUCCESS",
        "message": "Tìm thấy profile xung quanh",
        "profiles": profiles
    }
