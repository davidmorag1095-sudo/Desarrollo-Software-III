-- ============================================================
-- Script para crear la base de datos del proyecto de clientes
-- Ejecutar este archivo en MySQL Workbench
-- ============================================================

CREATE DATABASE IF NOT EXISTS empresa_clientes;

USE empresa_clientes;

CREATE TABLE IF NOT EXISTS clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cedula VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    direccion VARCHAR(200) NOT NULL
);

INSERT INTO clientes (cedula, nombre, correo, telefono, direccion)
VALUES
('101110111', 'Ana Pérez Mora', 'ana.perez@correo.com', '8888-1111', 'Puntarenas centro'),
('202220222', 'Carlos Rodríguez Solís', 'carlos.rodriguez@correo.com', '8888-2222', 'Barranca, Puntarenas'),
('303330333', 'María Gómez Castro', 'maria.gomez@correo.com', '8888-3333', 'El Roble, Puntarenas')
ON DUPLICATE KEY UPDATE nombre = nombre;

SELECT * FROM clientes;
