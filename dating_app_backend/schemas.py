# schemas.py
from pydantic import BaseModel
from typing import Optional, List


class UserBase(BaseModel):
    phone_number: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True


class SignupInput(BaseModel):
    username: str
    passwword: str 

class SignupOutput(BaseModel):
    id: str
    username: str
    code: str 
    message: str
    createdAt: str

class SigninInput(BaseModel):
    username: str
    password: str

class SigninOutput(BaseModel):
    token: str
    expireIn: str









# Đây là phần cho location
class NearbySearchInput(BaseModel):
    lat: str
    lng: str 
    radius: Optional[float] = 10

class ProfileInfo(BaseModel):
    id: str
    

class NearbySearchOutput(BaseModel):
    code: str 
    message: str 
    profiles: List[ProfileInfo]

class UpdateLocationInput(BaseModel):
    latitude: float
    longitude: float

class UpdateLocationOutput(BaseModel):
    success: bool


