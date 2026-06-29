from sqlalchemy import Column,Integer,String, ForeignKey

from config.database import Base

class DuenosORM(Base):
    __tablename__ = 'duenos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(Integer)
    email = Column(String(100))

    def  __repr__(self):
        return f"{self.nombre} {self.telefono} {self.email}"