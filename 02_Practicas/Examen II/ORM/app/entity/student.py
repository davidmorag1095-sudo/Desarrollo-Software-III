from ORM.app.config.database import Base

from sqlalchemy import Column, String, Integer

#studen hereda de base
class StudentORM(Base):
    __tablename__ = "students_tb"
    carnet= Column(String(20), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)


    #ejemplo de to string en java
    def __repr__(self):
        return f"Student(carnet='{self.carnet}', name='{self.name}', age='{self.age}')"
