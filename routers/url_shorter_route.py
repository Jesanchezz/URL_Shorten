from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from schema.url_schema import URLSchema
from database.Connection_db import get_db
from utilitys.short_url_generator import generate_short_url, url_finded


router_url_shorter = APIRouter(prefix="/api-url", tags=["URL Shorter"],
                               responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}})


@router_url_shorter.post("/shorten")
def create_url_short(url_input: URLSchema, db: Session = Depends(get_db)):
    url_created = generate_short_url(url_input, db)
    if not url_created:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Could not generate a unique short URL") 
    return url_created


@router_url_shorter.get("/redirect/{url_key}")
def redirect_url(url_key: str, db: Session = Depends(get_db)):
    url = url_finded(url_key, db)
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
    return RedirectResponse(url.original_url)