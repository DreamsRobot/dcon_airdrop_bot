from sqlalchemy import Column, Integer, String, BigInteger
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(BigInteger, unique=True)
    username = Column(String)
    wallet = Column(String, nullable=True)
    balance = Column(Integer, default=100)  # default bonus
    referrals = Column(Integer, default=0)
    referred_by = Column(BigInteger, nullable=True)
