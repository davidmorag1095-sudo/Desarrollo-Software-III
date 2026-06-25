from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#               SGBD-Driver://nombre_usuario:clave@direccion_ip:puerto/nombre_bd
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/students_db"
engine = create_engine(DATABASE_URL, echo = False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    #Importa las entidades para que SQLAchemy las registre
    Base.metadata.create_all(bind=engine)