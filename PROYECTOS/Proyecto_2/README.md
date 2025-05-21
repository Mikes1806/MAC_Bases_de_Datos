# Proyecto 2

## Descripción
• Este proyecto consiste en la creación de un lenguaje SQL personalizado que permite ejecutar operaciones básicas sobre archivos .csv como si fueran tablas de una base de datos relacional. 
• El lenguaje implementa los comandos: SELECT, INSERT, UPDATE, DELETE, y JOIN.
• No se utilizan archivos Parquet ni bibliotecas relacionadas, todo el manejo de datos se realiza directamente con archivos
.csv.

## Características
• Sintaxis similar a SQL tradicional
• Totalmente en Español.
• Soporte para los siguientes comandos:
   - SELECT: Consultas con proyección y condiciones.
   - INSERT: Inserción de registros.
   - UPDATE: Modificación de registros existentes.
   - DELETE: Eliminación de registros.
   - JOIN: Combinación de datos entre archivos .csv.
• Interfaz por línea de comandos.
• Parser y evaluador propio.

## Requisitos
• Python 3.10 (en adelante).
• Biblioteca estándar de Python:
   - os: para manejo del sistema de archivos.
   - csv: para lectura y escritura de archivos .csv.
   - re: para parseo con expresiones regulares.
• python-dotenv: para cargar variables de entorno desde un archivo .env.

## Configuración
• Crea el archivo **.env** en la raiz del proyecto, al mismo nivel que la carpeta **classes** y el **main.py**:
    PROYECTOS/
    ├── Proyecto_2/
        ├── class
        ├── main.py
        ├── **.env**

El contenido del archivo **.env** debe tener esta estructura:
DATA_PATH = C:\ruta\a\tu\carpeta\de\datos\PROYECTOS\Proyecto_2\classes\data

## Instalación y Uso
1. Clona el repositorio:
    git clone https://github.com/Mikes1806/MAC_Bases_de_Datos.git
2. Navega al directorio del proyecto:
    cd PROYECTOS/Proyecto_2
3. Ejecuta el comando:
    pip install python-dotenv
4. Ejecuta:
    python main.py

## Ejemplos de Consultas
• CREATE:
    crear tabla videojuego (id_videojuego INT,nombre VARCHAR,plataforma VARCHAR,horas_jugadas INT)
    crear tabla jugador (id_jugador INT,username VARCHAR,id_videojuego INT,fecha_juego DATE)
• INSERT:
    insertar en videojuego (id_videojuego,nombre,plataforma,horas_jugadas) valores (1,'Spiderman','PS5',45)
    insertar en videojuego (id_videojuego,nombre,plataforma,horas_jugadas) valores (2,'God of War 3','PS5',70)
    insertar en videojuego (id_videojuego,nombre,plataforma,horas_jugadas) valores (3,'Halo: Reach','Xbox',25)
    insertar en videojuego (id_videojuego,nombre,plataforma,horas_jugadas) valores (4,'Mario Strikers','Nintendo Switch',30)
    insertar en jugador (id_jugador,username,id_videojuego,fecha_juego) valores (1,'Jugador1',1,24/01/2025)
    insertar en jugador (id_jugador,username,id_videojuego,fecha_juego) valores (2,'Jugador2',2,10/12/2024)
• SELECT:
    seleccionar * de jugador
    seleccionar id_jugador,username,id_videojuego de jugador donde id_videojuego = 2
    seleccionar * de videojuego
    seleccionar id_videojuego,nombre,plataforma de videojuego donde plataforma = 'ps5'
• UPDATE:
    actualizar videojuego asignar plataforma = 'Xbox One' donde plataforma = 'Xbox'
    actualizar videojuego asignar horas_jugadas = 25 donde nombre = 'halo: reach'
• DELETE:
    eliminar de jugador donde id_videojuego = 3
    eliminar de videojuego donde plataforma = 'nintendo switch'
• JOIN:
    unir jugador con videojuego donde jugador.id_videojuego = videojuego.id_videojuego