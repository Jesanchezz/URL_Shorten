from fastapi import HTTPException
from schema.url_schema import URLSchema
import secrets
import string
from sqlalchemy.orm import Session
from database.Models import urls

def register_url_data(original_url:str, short_url:str, db:Session):
    new_url = urls(original_url=original_url, short_url=short_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    return True 

def is_unique_url(short_url:str, db:Session):
    stored_url = db.query(urls).filter(urls.short_url == short_url).first()
    if not stored_url:
        return True
    return False

def generate_short_url(url_input: URLSchema, db: Session, length: int = 10):
    characters = string.ascii_letters + string.digits
    short_url_created = ''.join(secrets.choice(characters) for _ in range(length))

    if is_unique_url(short_url_created, db):
        if not register_url_data(url_input.url, short_url_created, db):
            raise HTTPException(status_code=500, detail="Error registering short URL")
        return {"new_url": short_url_created}
    else:
        return generate_short_url(url_input, db, length)


def url_finded(url_key: str, db: Session):
    return db.query(urls).filter(urls.short_url == url_key).first()