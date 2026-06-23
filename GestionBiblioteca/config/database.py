from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "mysql+pymysql://root:@localhost:3306/biblioteca_db"

engine = create_engine(DATABASE_URI, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

