from sqlalchemy import Column, String, Integer
from ORM.app.config.database import Base

class StudentORM(Base):
    __tablename__ = "student"

    carnet = Column(String(20), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

    def __repr__(self):
        return f"Student(carnet='{self.carnet}', name='{self.name}', age='{self.age}')"