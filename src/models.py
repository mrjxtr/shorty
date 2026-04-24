from sqlalchemy import Column, Integer, String, DateTime  # Datatypes
from datetime import datetime, timezone # work w/ date/time
from database import Base


# Defining table in db
class URL(Base):
    __tablename__ = "urls"  

    # --Defining cols

    id = Column(Integer, primary_key=True, index=True)
    # primary_ket -> main identifier
    # index -> lookup by id

    short_code = Column(String, unique=True, index=True)
    # unique -> no duplicates

    original_url = Column(String, nullable=False)
    # nullable -> can be null

    created_at = Column(DateTime, default=datetime.now(timezone.utc))  # use UTC instead of local
    # datetime.now -> current local time

