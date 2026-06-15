-- ============================================================
-- Script para crear la base de datos del proyecto
-- Ejecutar este archivo en MySQL Workbench
-- ============================================================

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS universidad;

-- Seleccionar la base de datos que se va a utilizar
USE universidad;

-- Crear la tabla estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    carrera VARCHAR(100) NOT NULL
);

-- Insertar datos de prueba opcionales
-- Estos datos sirven para verificar que la tabla funciona correctamente
INSERT INTO estudiantes (nombre, correo, carrera)
VALUES 
('Ana Pérez', 'ana.perez@ucr.ac.cr', 'Ingeniería Eléctrica'),
('Carlos Mora', 'carlos.mora@ucr.ac.cr', 'Ingeniería Electromecánica')
ON DUPLICATE KEY UPDATE nombre = nombre;

-- Consultar los datos registrados
SELECT * FROM estudiantes;
