from app.config.database_conexion import SessionLocal
from app.entity.mascotasORM import MascotasORM


class RepositoryMascotas:

    def __init__(self):
        self.db = SessionLocal()

    def save(self, codigo, nombre, especie, edad, dueno_id):
        mascota = MascotasORM(
            codigo=codigo,
            nombre=nombre,
            especie=especie,
            edad=edad,
            dueno_id=dueno_id
        )
        self.db.add(mascota)
        self.db.commit()
        return mascota

    def get(self, codigo):
        return self.db.query(MascotasORM).filter_by(codigo=codigo).first()

    def get_all(self):
        return self.db.query(MascotasORM).all()

    def update(self, codigo, nombre, especie, edad, dueno_id):
        mascota = self.get(codigo)
        if mascota:
            mascota.nombre = nombre
            mascota.especie = especie
            mascota.edad = edad
            mascota.dueno_id = dueno_id
            self.db.commit()
            self.db.refresh(mascota)
        return mascota

    def delete(self, codigo):
        mascota = self.get(codigo)
        if mascota:
            self.db.delete(mascota)
            self.db.commit()
        return mascota

    def existe_dueno_con_mascota(self, id):
        return self.db.query(MascotasORM).filter_by(dueno_id=id).first() is not None

    def count_by_especie(self):
        from sqlalchemy import func

        return self.db.query(
            MascotasORM.especie,
            func.count(MascotasORM.codigo)
        ).group_by(MascotasORM.especie).all()

