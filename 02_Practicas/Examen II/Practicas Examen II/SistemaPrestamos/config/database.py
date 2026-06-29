from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/prestamos_equipos_db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    from entity.equipo_entity import EquipoORM
    from entity.estudiante_entity import EstudianteORM
    from entity.prestamo_entity import PrestamoORM
    from entity.categoria_entity import CategoriaORM
    Base.metadata.create_all(engine)