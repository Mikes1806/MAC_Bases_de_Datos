-- Crear ROLES GENERALES
CREATE ROLE rol_ddl;
CREATE ROLE rol_dml;
CREATE ROLE rol_read;
CREATE ROLE rol_write;

-- Crear USUARIOS y asignar contraseña
CREATE ROLE user_ddl1 WITH LOGIN PASSWORD 'ddl123';
CREATE ROLE user_dml1 WITH LOGIN PASSWORD 'dml123';
CREATE ROLE user_read1 WITH LOGIN PASSWORD 'read123';
CREATE ROLE user_read2 WITH LOGIN PASSWORD 'read456';
CREATE ROLE user_read3 WITH LOGIN PASSWORD 'read789';
CREATE ROLE user_write1 WITH LOGIN PASSWORD 'write123';
CREATE ROLE user_write2 WITH LOGIN PASSWORD 'write456';

-- Asignar ROLES a usuarios
GRANT rol_ddl TO user_ddl1;
GRANT rol_dml TO user_dml1;
GRANT rol_read TO user_read1, user_read2, user_read3;
GRANT rol_write TO user_write1, user_write2;

-- Crear ESQUEMAS
CREATE SCHEMA esquema1 AUTHORIZATION rol_ddl;
CREATE SCHEMA esquema2 AUTHORIZATION rol_ddl;

-- CREAR TABLAS dentro de esquema1 (el owner es rol_ddl)
SET ROLE rol_ddl;

-- Esquema 1: videojuegos
CREATE TABLE IF NOT EXISTS esquema1.juegos (
    id SERIAL PRIMARY KEY,
    nombre_juego VARCHAR(255) NOT NULL,
    horas_jugadas INT NOT NULL,
    plataforma VARCHAR(50) NOT NULL,
    porcentaje_progreso INT NOT NULL,
    status VARCHAR(50) NOT NULL
);

-- Esquema 2: estadísticas generales
CREATE VIEW esquema2.view_estadisticas_generales AS
SELECT
    COUNT(*) AS total_juegos,           -- Total de juegos en la tabla
    AVG(horas_jugadas) AS promedio_horas -- Promedio de horas jugadas
FROM esquema1.juegos;

RESET ROLE;

-- Asignar PERMISOS por esquema

-- Esquema 1
GRANT USAGE ON SCHEMA esquema1 TO rol_dml, rol_read, rol_write;
GRANT SELECT ON ALL TABLES IN SCHEMA esquema1 TO rol_read;
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA esquema1 TO rol_write;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA esquema1 TO rol_dml;

-- Esquema 2
GRANT USAGE ON SCHEMA esquema2 TO rol_read;
GRANT SELECT ON ALL TABLES IN SCHEMA esquema2 TO rol_read;

-- Nota: como las tablas fueron creadas por el rol DDL, este es el owner de todas