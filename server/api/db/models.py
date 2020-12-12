from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
	__tablename__ = "users"
	
	id = Column(Integer, primary_key=True, index=True)
	name = Column(String, unique=True, index=True)
	wins = Column(Integer)
	losses = Column(Integer)
	num_games = Column(Integer)
