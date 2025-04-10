# # models.py
# from sqlalchemy import Column, Integer, String
# from database import Base

# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     phone_number = Column(String, unique=True, index=True)
#     password = Column(String)


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from database import Base


# Bảng Users
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    password = Column(String)
    username = Column(String)
    email = Column(String)
    created_at = Column(String)
    updated_at = Column(String)


class UserLocation(Base):
    __tablename__ = "user_locations"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    lat = Column(Float)
    lng = Column(Float)






# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, Text, Float
# from sqlalchemy.orm import relationship
# from database import Base
# from datetime import datetime

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     phone_number = Column(String(15), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     username = Column(String(50), nullable=False)
#     email = Column(String(100), nullable=True)
#     role = Column(String(20), default='user')
#     active = Column(Boolean, default=True)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)

#     profile = relationship('Profile', back_populates='user', uselist=False)
#     images = relationship('Image', back_populates='user')
#     likes = relationship('Like', back_populates='user')
#     reports = relationship('Report', back_populates='user')
#     messages_sent = relationship('Message', foreign_keys='Message.sender_id', back_populates='sender')
#     messages_received = relationship('Message', foreign_keys='Message.receiver_id', back_populates='receiver')

# class Profile(Base):
#     __tablename__ = 'profiles'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), unique=True)
#     gender = Column(String(10), nullable=True)
#     birth_date = Column(TIMESTAMP, nullable=True)
#     bio = Column(Text, nullable=True)
#     location = Column(String(100), nullable=True)
#     gender_preference = Column(String(10), nullable=True)
#     min_age = Column(Integer, nullable=True)
#     max_age = Column(Integer, nullable=True)
#     distance_range_km = Column(Integer, nullable=True)
#     avatar = Column(Text, nullable=True)

#     user = relationship('User', back_populates='profile')




# class Image(Base):
#     __tablename__ = 'images'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     title = Column(String(100), nullable=True)
#     url = Column(Text, nullable=False)
#     uploaded_at = Column(TIMESTAMP, default=datetime.utcnow)

#     user = relationship('User', back_populates='images')

# class Like(Base):
#     __tablename__ = 'likes'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     target_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     status = Column(String(10), nullable=False)
#     timestamp = Column(TIMESTAMP, default=datetime.utcnow)

#     user = relationship('User', foreign_keys=[user_id], back_populates='likes')

# class Match(Base):
#     __tablename__ = 'matches'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id_1 = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     user_id_2 = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     matched_at = Column(TIMESTAMP, default=datetime.utcnow)

# class Report(Base):
#     __tablename__ = 'reports'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     target_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     reason = Column(Text, nullable=False)
#     content = Column(Text, nullable=True)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)

#     user = relationship('User', back_populates='reports')

# class Message(Base):
#     __tablename__ = 'messages'

#     id = Column(Integer, primary_key=True, index=True)
#     sender_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     receiver_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     content = Column(Text, nullable=False)
#     timestamp = Column(TIMESTAMP, default=datetime.utcnow)

#     sender = relationship('User', foreign_keys=[sender_id], back_populates='messages_sent')
#     receiver = relationship('User', foreign_keys=[receiver_id], back_populates='messages_received')

# class Conversation(Base):
#     __tablename__ = 'conversations'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id_1 = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     user_id_2 = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)

# class Notification(Base):
#     __tablename__ = 'notifications'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     message = Column(Text, nullable=False)
#     is_read = Column(Boolean, default=False)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)

# class Location(Base):
#     __tablename__ = 'locations'

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
#     latitude = Column(Float, nullable=False)
#     longitude = Column(Float, nullable=False)
#     updated_at = Column(TIMESTAMP, default=datetime.utcnow)
