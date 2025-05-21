CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE tiendas_poligono (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cobertura GEOMETRY(POLYGON, 4326)
);

INSERT INTO tiendas_poligono(nombre, cobertura)
VALUES 
('Tienda x', ST_GeomFromText(
  'POLYGON((
    -99.1332 19.4371,
    -99.1287 19.4341,
    -99.1296 19.4280,
    -99.1368 19.4280,
    -99.1377 19.4341,
    -99.1332 19.4371))', 4326)),

('3B', ST_GeomFromText(
  'POLYGON((
    -99.1512 19.5046,
    -99.1467 19.5016,
    -99.1476 19.4955,
    -99.1548 19.4955,
    -99.1557 19.5016,
    -99.1512 19.5046))', 4326)),

('OXXO', ST_GeomFromText(
  'POLYGON((
    -99.1321 19.3549,
    -99.1276 19.3519,
    -99.1285 19.3458,
    -99.1357 19.3458,
    -99.1366 19.3519,
    -99.1321 19.3549))', 4326)),

('GARIS', ST_GeomFromText(
  'POLYGON((
    -99.0800 19.4345,
    -99.0755 19.4315,
    -99.0764 19.4254,
    -99.0836 19.4254,
    -99.0845 19.4315,
    -99.0800 19.4345))', 4326)),

('COSCO', ST_GeomFromText(
  'POLYGON((
    -99.2000 19.4445,
    -99.1955 19.4415,
    -99.1964 19.4354,
    -99.2036 19.4354,
    -99.2045 19.4415,
    -99.2000 19.4445))', 4326));


select nombre
from tiendas_poligono
where St_intersects(cobertura,
ST_setSRID(ST_MakePoint(-99.1332, 19.4326),4326));


select nombre, ST_Distance(cobertura, ST_SetSRID(ST_MakePoint(-99.1332, 19.4326),4326)) as distacia_metros from tiendas_poligono
where ST_DWithin (cobertura, ST_SetSRID(ST_MakePoint(-99.1332, 19.4326),4326),1000);

 