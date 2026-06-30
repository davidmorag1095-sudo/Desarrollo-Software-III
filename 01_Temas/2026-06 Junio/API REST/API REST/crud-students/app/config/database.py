from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Skull_fab%4019@localhost:3306/students_db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    # Import entities so SQLAlchemy registers them
    from app.entity.student import StudentORM
    Base.metadata.create_all(bind=engine)
