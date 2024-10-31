# models/habit.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, Session

class Habit(Base):
    __tablename__ = 'habits'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    frequency = Column(String, nullable=False)  # e.g., daily, weekly, etc.
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship
    user = relationship("User", back_populates="habits")

    @classmethod
    def create(cls, name, frequency, user_id):
        session = Session()
        habit = cls(name=name, frequency=frequency, user_id=user_id)
        session.add(habit)
        session.commit()
        session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        habits = session.query(cls).all()
        session.close()
        return habits

    @classmethod
    def find_by_id(cls, habit_id):
        session = Session()
        habit = session.query(cls).get(habit_id)
        session.close()
        return habit

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()
