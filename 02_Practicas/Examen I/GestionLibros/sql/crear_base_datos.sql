CREATE DATABASE IF NOT EXISTS biblioteca;

USE biblioteca;

CREATE TABLE IF NOT EXISTS libros (
    codigo VARCHAR(10) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);

-- Datos de prueba
INSERT INTO libros (codigo, titulo, autor, categoria)
VALUES
('L001', 'El Principito', 'Antoine de Saint-Exupery', 'Literatura'),
('L002', 'Cien anos de soledad', 'Gabriel Garcia Marquez', 'Novela')
ON DUPLICATE KEY UPDATE codigo = codigo;

SELECT * FROM libros;
