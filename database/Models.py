from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class urls(Base):
    __tablename__ = 'urls'

    id_url = Column(Integer, primary_key=True, autoincrement=True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)