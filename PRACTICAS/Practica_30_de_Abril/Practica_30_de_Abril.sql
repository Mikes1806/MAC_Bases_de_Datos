
CREATE TABLE equipo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    estadio VARCHAR(50),
    capacidad INT,
    fundacion INT, 
    titulos INT DEFAULT 0
);


CREATE TABLE partido (
    id SERIAL PRIMARY KEY,
    equipo_visitante INT NOT NULL,
    equipo_local INT NOT NULL,
    estadio VARCHAR(50),
    fecha DATE NOT NULL, 
    equipo_ganador INT NULL,  -- Puede ser NULL en caso de empate
    equipo_perdedor INT NULL, -- Puede ser NULL en caso de empate
    FOREIGN KEY (equipo_visitante) REFERENCES equipo(id),
    FOREIGN KEY (equipo_local) REFERENCES equipo(id),
    FOREIGN KEY (equipo_ganador) REFERENCES equipo(id),
    FOREIGN KEY (equipo_perdedor) REFERENCES equipo(id) 
);

-- Creación de la tabla jugador
CREATE TABLE jugador (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    nacionalidad VARCHAR(50),
    posicion VARCHAR(30),
    equipo_id INT NOT NULL,
    numero_camiseta INT CHECK (numero_camiseta BETWEEN 1 AND 99),
    FOREIGN KEY (equipo_id) REFERENCES equipo(id) 
);

CREATE TABLE alineacion (
    id SERIAL PRIMARY KEY,
    partido_id INT NOT NULL,
    jugador_id INT NOT NULL,
    FOREIGN KEY (partido_id) REFERENCES partido(id),
    FOREIGN KEY (jugador_id) REFERENCES jugador(id)
);


INSERT INTO equipo (nombre, ciudad, estadio, capacidad, fundacion, titulos) VALUES
('Real Madrid', 'Madrid', 'Santiago Bernabéu', 81044, 1902, 35),
('FC Barcelona', 'Barcelona', 'Camp Nou', 99354, 1899, 27),
('Manchester United', 'Manchester', 'Old Trafford', 74310, 1878, 20),
('Bayern Munich', 'Múnich', 'Allianz Arena', 75000, 1900, 33),
('Juventus', 'Turín', 'Allianz Stadium', 41507, 1897, 36);


INSERT INTO partido (equipo_visitante, equipo_local, estadio, fecha, equipo_ganador, equipo_perdedor) VALUES
(1, 2, 'Santiago Bernabéu', '2024-03-15', 1, 2),
(3, 4, 'Allianz Arena', '2024-04-10', 4, 3),
(5, 1, 'Santiago Bernabéu', '2024-05-05', 1, 5),
(2, 3, 'Old Trafford', '2024-06-20', 3, 2),
(4, 5, 'Allianz Stadium', '2024-07-12', 5, 4);


INSERT INTO jugador (nombre, fecha_nacimiento, nacionalidad, posicion, equipo_id, numero_camiseta) VALUES
('Karim Benzema', '1987-12-19', 'Francia', 'Delantero', 1, 9),
('Lionel Messi', '1987-06-24', 'Argentina', 'Delantero', 2, 10),
('Bruno Fernandes', '1994-09-08', 'Portugal', 'Centrocampista', 3, 8),
('Robert Lewandowski', '1988-08-21', 'Polonia', 'Delantero', 4, 9),
('Cristiano Ronaldo', '1985-02-05', 'Portugal', 'Delantero', 5, 7);


SELECT e.nombre, COUNT(p.equipo_ganador) AS total_victorias
FROM equipo e
JOIN partido p ON e.id = p.equipo_ganador
GROUP BY e.id
ORDER BY total_victorias DESC
LIMIT 1;


SELECT e.ciudad, COUNT(p.id) AS total_partidos
FROM equipo e
JOIN partido p ON e.estadio = p.estadio
GROUP BY e.ciudad
ORDER BY total_partidos DESC
LIMIT 1;


SELECT j.nombre, COUNT(a.partido_id) AS total_partidos
FROM jugador j
JOIN alineacion a ON j.id = a.jugador_id
GROUP BY j.id
ORDER BY total_partidos DESC
LIMIT 1;



