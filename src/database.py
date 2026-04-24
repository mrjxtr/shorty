from sqlalchemy import create_engine  # connection to db
from sqlalchemy.ext.declarative import declarative_base  # base class
from sqlalchemy.orm import sessionmaker   # create session when interacting w/ db
from dotenv import load_dotenv  # read from .env
import os  #  interact w/ os -> read from load_dotenv

load_dotenv()  # load from .env

DATABASE_URL = os.getenv("DATABASE_URL")  # grab from .env file

engine = create_engine(DATABASE_URL)  # actual connection to postgres

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # session
# autocommit=F -> change in db not autocommit
# autoflush=F -> won't auto send pending changees to db
# bind=engine -> connect this sess to db engine

Base = declarative_base()  # base class all models will inherit from

def get_db():  # called when accessing db
    db = SessionLocal()  # create session
    try:
        yield db  # hands session
    finally:
        db.close()  # always close after every session