-- Crear ROLES GENERALES
CREATE ROLE rol_ddl;
CREATE ROLE rol_dml;
CREATE ROLE rol_read;
CREATE ROLE rol_write;

-- Crear USUARIOS y asignar contraseña
CREATE ROLE user_ddl1 WITH LOGIN PASSWORD ---;
CREATE ROLE user_dml1 WITH LOGIN PASSWORD ---;
CREATE ROLE user_read1 WITH LOGIN PASSWORD ---;
CREATE ROLE user_read2 WITH LOGIN PASSWORD ---;
CREATE ROLE user_read3 WITH LOGIN PASSWORD ---;
CREATE ROLE user_write1 WITH LOGIN PASSWORD ---;
CREATE ROLE user_write2 WITH LOGIN PASSWORD ---;

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
CREATE OR REPLACE VIEW esquema2.view_estadisticas_generales AS
SELECT
    COUNT(*) AS total_juegos,
    AVG(horas_jugadas) AS promedio_horas,
    AVG(porcentaje_progreso) AS promedio_progreso
FROM esquema1.juegos;


RESET ROLE;

-- Asignar PERMISOS por rol

-- DML
GRANT USAGE ON SCHEMA esquema1 TO rol_dml;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA esquema1 TO rol_dml;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA esquema1 TO rol_dml;

-- READ
GRANT USAGE ON SCHEMA esquema1, esquema2 TO rol_read;
GRANT SELECT ON ALL TABLES IN SCHEMA esquema1 TO rol_read;
GRANT SELECT ON ALL TABLES IN SCHEMA esquema2 TO rol_read;

-- WRITE
GRANT USAGE ON SCHEMA esquema1 TO rol_write;
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA esquema1 TO rol_write;
GRANT USAGE, SELECT, UPDATE ON ALL SEQUENCES IN SCHEMA esquema1 TO rol_write;

-- Los demás roles no pueden dar permisos
REVOKE GRANT OPTION FOR ALL ON ALL TABLES IN SCHEMA esquema1 FROM rol_dml, rol_write, rol_read;
REVOKE GRANT OPTION FOR ALL ON ALL SEQUENCES IN SCHEMA esquema1 FROM rol_dml, rol_write;

-- Nota: como las tablas fueron creadas por el rol DDL, este es el owner de todas