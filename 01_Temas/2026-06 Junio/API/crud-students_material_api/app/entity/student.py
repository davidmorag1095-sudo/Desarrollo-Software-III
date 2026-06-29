from sqlalchemy import Column, String, Integer

from app.config.database import Base


class StudentORM(Base):
    __tablename__ = "students_tb"

    carnet = Column(String(20), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)

    def __repr__(self):
        return f"Student(carnet='{self.carnet}', name='{self.name}', age={self.age})"

