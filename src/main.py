from fastapi import (
    FastAPI,
    Depends,  # dependency
    status,  # HTTP dynamic status codes
    HTTPException  # raising HTTP error
) 
from fastapi.responses import RedirectResponse  # redirecting
from sqlalchemy.orm import Session
from database import engine, get_db  # connection to db  # access db function
from pydantic import (
    BaseModel,  # schema
    HttpUrl  # validating url

 ) 
import models  # models.py
from random import choices  # allow duplication
from string import (
    ascii_letters,  # string of letters
    digits  # string of numbers
)


app = FastAPI()

models.Base.metadata.create_all(bind=engine)  # auto create db


class ShortyPost(BaseModel):
    long_url: HttpUrl


# --------------
# UTILS
# --------------
def generate_code(LENGTH=6):
    characters = ascii_letters + digits  # pool of alphanum
    return "".join(choices(characters, k=LENGTH))  # join 6 chosen characters



# --------------
# ENDPOINTS
# --------------


# Test root
@app.get("/", status_code=status.HTTP_200_OK)
def test():
    return {"message": "connected"}


# Get all entries
@app.get("/all", status_code=status.HTTP_200_OK)
def get_all_entries(db: Session = Depends(get_db)):
    query = db.query(models.URL)
    entries = query.all()
    return {"entries": entries}



# Return short code
@app.post("/shorten", status_code=status.HTTP_201_CREATED)
def shorten_url(original_url: ShortyPost, db: Session = Depends(get_db)):  # receive long url
    
    short_code = generate_code()  # short code

    url = str(original_url.long_url)  # long url
    # convert Url obj to string

    entry = models.URL(short_code=short_code, original_url=url)

    # save to db
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {"short code": short_code}



# Redirect to url
@app.get("/{short_code}") # receive short code
def redirect(short_code: str, db: Session = Depends(get_db)):
    
    # check if existing in db
    query = db.query(models.URL).filter(models.URL.short_code == short_code)
    entry = query.first()

    if not entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="code not found")

    return RedirectResponse(url=entry.original_url)



