# app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.types import Date
#from my_database import Base,engine,SessionLocal
from sqlalchemy.orm import relationship


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "sqlite:///./my_database.db"  # Use your database URL here

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()


class UserCreate(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)  
    username = Column(String, index=True)
    email = Column(String, index = True,unique=True)  #change to unique
    password = Column(String, index=True)
    
try:
    Base.metadata.create_all(engine)

except Exception as e:
    print(f"Error creating tables: {e}")