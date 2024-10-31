# models/task.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, Session

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationship
    user = relationship("User", back_populates="tasks")

    @classmethod
    def create(cls, title, description, user_id):
        session = Session()
        task = cls(title=title, description=description, user_id=user_id)
        session.add(task)
        session.commit()
        session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        tasks = session.query(cls).all()
        session.close()
        return tasks

    @classmethod
    def find_by_id(cls, task_id):
        session = Session()
        task = session.query(cls).get(task_id)
        session.close()
        return task

    def delete(self):
        session = Session()
        session.delete(self)
        session.commit()
        session.close()
