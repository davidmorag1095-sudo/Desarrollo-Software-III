# Proyecto MySQL Clientes con Consola y Web

Proyecto didáctico para trabajar conexión de Python con una base de datos MySQL real desde PyCharm.

Esta versión permite hacer el CRUD de clientes de dos formas:

1. Desde consola con `main.py`.
2. Desde una página web con Flask usando `app.py`.

Ambas opciones usan la misma lógica del sistema:

- `model`
- `repository`
- `service`
- `database`

## Requisitos

1. Tener instalado Python.
2. Tener instalado PyCharm.
3. Tener instalado MySQL Server.
4. Tener instalado MySQL Workbench.
5. Instalar las librerías necesarias:

```bash
pip install -r requirements.txt
```

## Crear la base de datos

Abra MySQL Workbench y ejecute el archivo:

```text
sql/crear_base_datos_clientes.sql
```

Ese script crea:

- Base de datos `empresa_clientes`
- Tabla `clientes`
- Algunos datos de prueba opcionales

## Configurar la conexión

Abra el archivo:

```text
database/conexion.py
```

Y revise estos datos:

```python
host="localhost"
user="root"
password="12345"
database="empresa_clientes"
port=3306
```

Debe cambiar `password="12345"` por la contraseña real de MySQL en su computadora.

## Ejecutar versión por consola

Ejecute el archivo:

```text
main.py
```

## Ejecutar versión web

Ejecute el archivo:

```text
app.py
```

Luego abra el navegador y entre a:

```text
http://127.0.0.1:5000
```

## Flujo web

```text
HTML → Flask app.py → Service → Repository → MySQL
```

El HTML no se conecta directamente a MySQL. Flask recibe los formularios y llama la misma lógica usada por consola.
