# Proyecto MySQL Estudiantes

Proyecto didáctico para trabajar conexión de Python con una base de datos MySQL real desde PyCharm.

## Requisitos

1. Tener instalado Python.
2. Tener instalado PyCharm.
3. Tener instalado MySQL Server.
4. Tener instalado MySQL Workbench.
5. Instalar la librería de conexión:

```bash
pip install mysql-connector-python
```

## Pasos para usar el proyecto

### 1. Crear la base de datos en MySQL Workbench

Abra MySQL Workbench y ejecute el archivo:

```text
sql/crear_base_datos.sql
```

Ese script crea:

- Base de datos `universidad`
- Tabla `estudiantes`

### 2. Revisar usuario y contraseña

Abra el archivo:

```text
database/conexion.py
```

Y cambie estos datos según su instalación de MySQL:

```python
user="root"
password="12345"
```

Si su contraseña de MySQL es diferente, debe modificarla.

### 3. Abrir el proyecto en PyCharm

Abra la carpeta completa del proyecto:

```text
proyecto_mysql_estudiantes
```

### 4. Ejecutar el programa

Ejecute el archivo:

```text
main.py
```

## Funcionalidades

El sistema permite:

1. Registrar estudiante.
2. Consultar todos los estudiantes.
3. Buscar estudiante por ID.
4. Actualizar datos de estudiante.
5. Eliminar estudiante.
6. Salir.

## Estructura del proyecto

```text
proyecto_mysql_estudiantes/
│
├── main.py
├── requirements.txt
│
├── sql/
│   └── crear_base_datos.sql
│
├── database/
│   └── conexion.py
│
├── model/
│   └── estudiante.py
│
├── repository/
│   └── estudiante_repository.py
│
├── service/
│   └── estudiante_service.py
│
└── controller/
    └── estudiante_controller.py
```

## Explicación de capas

| Capa | Función |
|---|---|
| `model` | Representa los datos del estudiante |
| `database` | Maneja la conexión con MySQL |
| `repository` | Ejecuta las consultas SQL |
| `service` | Valida reglas de negocio |
| `controller` | Coordina el menú con la lógica |
| `main.py` | Punto de inicio del programa |
