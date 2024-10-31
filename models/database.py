# models/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tracker.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()

def initialize_db():
    Base.metadata.create_all(engine)
