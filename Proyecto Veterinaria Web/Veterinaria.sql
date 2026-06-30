-- Base de datos para el proyecto Clinica Veterinaria

CREATE DATABASE clinica_veterinaria_db;

USE clinica_veterinaria_db;

CREATE TABLE IF NOT EXISTS duenos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS mascotas (
    codigo VARCHAR(100) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especie VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    dueno_id INT NOT NULL,
    CONSTRAINT fk_mascotas_duenos
        FOREIGN KEY (dueno_id) REFERENCES duenos(id)
);

CREATE TABLE IF NOT EXISTS citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_mascota VARCHAR(100) NOT NULL,
    fecha VARCHAR(10) NOT NULL,
    hora VARCHAR(5) NOT NULL,
    motivo VARCHAR(150) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    CONSTRAINT fk_citas_mascotas
        FOREIGN KEY (codigo_mascota) REFERENCES mascotas(codigo)
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    clave VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (usuario, clave)
SELECT 'admin', 'admin123'
WHERE NOT EXISTS (
    SELECT 1 FROM usuarios WHERE usuario = 'admin'
);

