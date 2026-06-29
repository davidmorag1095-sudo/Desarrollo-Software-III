from config.database import SessionLocal
from entity.mascota import MascotaORM

class MascotaRepository():
    def __init__(self):
        self.db = SessionLocal()

    def registar_mascota(self, codigo, nombre, especie, edad, dueno_id):
        mascota = MascotaORM(codigo = codigo, nombre = nombre, especie = especie, edad = edad, dueno_id = dueno_id)
        self.db.add(mascota)
        self.db.commit()
        return mascota
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(MascotaORM).all()

#---------------------------------------------------------------------------------------------------------
    def get_by_codigo(self, codigo):
        return self.db.query(MascotaORM).filter_by(codigo = codigo).first()
#---------------------------------------------------------------------------------------------------------
    def update(self, codigo, nombre, especie, edad, dueno_id):
        mascota = self.get_by_codigo(codigo)

        if mascota:
            mascota.nombre = nombre
            mascota.edad = edad
            mascota.especie = especie
            mascota.dueno_id = dueno_id
            self.db.commit()
        return mascota
#---------------------------------------------------------------------------------------------------------

    def delete_pet(self, codigo):
        mascota = self.get_by_codigo(codigo)

        if mascota:
            self.db.delete(mascota)
            self.db.commit()
        return mascota
#---------------------------------------------------------------------------------------------------------
    def existe_dueno_con_mascota(self, id):
        return self.db.query(MascotaORM).filter_by(dueno_id=id).first() is not None

