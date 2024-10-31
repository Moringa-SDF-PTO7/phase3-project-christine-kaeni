# models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base, Session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    # Relationships
    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    habits = relationship("Habit", back_populates="user", cascade="all, delete")

    @classmethod
    def create(cls, name, email):
        session = Session()
        user = cls(name=name, email=email)
        session.add(user)
        session.commit()
        session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        users = session.query(cls).all()
        session.close()
        return users

    @classmethod
    def find_by_id(cls, user_id):
        session = Session()
        user = session.query(cls).get(user_id)
        session.close()
        return user

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()
