# CRUD Clínica Veterinaria

## Base de datos

Crear en MySQL la base de datos:

```sql
CREATE DATABASE clinica_veterinaria_db;
```

La conexión se encuentra en `app/config/database_conexion.py`.

## Ejecutar

Desde esta carpeta:

```bash
uvicorn app.main:app --reload
```

La documentación de la API estará en `http://127.0.0.1:8000/docs`.

Usuario inicial:

- Usuario: `admin`
- Contraseña: `admin123`

