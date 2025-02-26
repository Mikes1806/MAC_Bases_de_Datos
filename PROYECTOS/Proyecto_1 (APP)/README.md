# MyGames

## Descripción
Esta aplicación permite llevar un registro de tus videojuegos, facilitando el seguimiento de los títulos que juegas, horas de juego, plataformas, y más.

## Características
• Registro de videojuegos jugados.
• Gestión de plataformas (PC, Xbox, PlayStation, etc.).
• Seguimiento de horas jugadas por cada juego.

## Tecnologías utilizadas

• **Frontend:** Streamlit
• **Backend:** Python
• **Base de Datos:** PostgreSQL / MySQL
• **Contenerización:** Docker

## Requisitos previos
1. Es recomendable usar **Git Bash** para ejecutar los comandos en este proyecto, ya que ofrece una mejor compatibilidad con las herramientas de línea de comandos que podrían no funcionar correctamente en **PowerShell**.

2. Asegúrate de tener **Docker** instalado en tu sistema.

3. Necesitarás tener acceso a una base de datos **PostgreSQL** y **MySQL** para almacenar tanto al usuario de la aplicación como los registros de videojuegos respectivamente.
Opcional: Tener un administrador de bases de datos configurado (como **DBeaver**).

## Pasos para correr la aplicación
1. Clona el repositorio:
    git clone https://github.com/Mikes1806/MAC_Bases_de_Datos.git
2. Navega al directorio del proyecto:
    cd PROYECTOS/Proyecto_1\ \(APP\)/
3. Ejecuta el comando:
    source Launcher.sh
4. Accede a la aplicación abriendo tu navegador y dirigiéndote a:
    http://localhost:8501 

## Configuración
1. Antes de ejecutar los contenedores con Docker, asegúrate de que los servicios de MySQL y PostgreSQL no estén en ejecución en tu máquina local. Esto evitará conflictos de puertos. Si tienes los servicios corriendo, por favor, deténlos de la siguiente manera (Windows):
    • **MySQL:** Ejecuta la combinación de teclas "Windows + r", escribe "services.msc", busca "MySQL" y selecciona "Detener".
    • **PostgreSQL:** Ejecuta la combinación de teclas "Windows + r", escribe "services.msc", busca "MySQL" y selecciona "Detener".

2. Crea los archivos **.env**, **my.cnf**, **init_mysql.sql**, **init_postgres.sql** e **init_table_mysql.sql** en la raiz del proyecto, al mismo nivel que el **Dockerfile** y el **requirements.txt**:
    PROYECTOS/
    ├── Proyecto_1/
        ├── Dockerfile
        ├── requirements.txt
        ├── **.env**
        ├── **init_mysql.sql**
        ├── **init_postgres.sql**
        ├── **init_table_mysql.sql**
        └── **my.cnf**

El contenido del archivo **.env** debe tener esta estructura:
    #Credenciales de la conexión de Postgres
    POSTGRES_HOST = postgres_db
    POSTGRES_DB = nombre_de_tu_base_de_datos
    POSTGRES_USER = usuario_postgres
    POSTGRES_PASSWORD = contraseña_segura

    #Credenciales de la conexión de MySQL
    MYSQL_HOST = mysql_db
    MYSQL_DB = nombre_de_tu_base_de_datos
    MYSQL_USER = usuario_mysql
    MYSQL_PASSWORD = contraseña_segura
    MYSQL_ROOT_PASSWORD = contraseña_mas_segura

El contenido del archivo **init_mysql.sql** debe tener la siguiente estructura:
    -- Crear base de datos si no existe
    CREATE DATABASE IF NOT EXISTS nombre_de_tu_base_de_datos;

    -- Crear usuario si no existe
    CREATE USER IF NOT EXISTS 'usuario_mysql'@'%' IDENTIFIED BY 'contraseña_segura';

    -- Otorgar todos los privilegios al usuario sobre la base de datos
    GRANT ALL PRIVILEGES ON nombre_de_tu_base_de_datos.* TO 'usuario_mysql'@'%';

    -- Aplicar cambios
    FLUSH PRIVILEGES;

El contenido del archivo **init_postgres.sql** debe tener la siguiente estructura:
    -- Crear tabla para los usuarios
    CREATE TABLE usuarios (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );

    -- Insertar el usuario para usar la aplicación
    INSERT INTO usuarios (username, password) VALUES ('user_mygames', 'password_mygames');

El contenido del archivo **init_table_mysql.sql** debe tener la siguiente estructura:
    -- Verifica la base de datos
    CREATE DATABASE IF NOT EXISTS nombre_de_tu_base_de_datos;
    USE nombre_de_tu_base_de_datos;

    -- Crear tabla para los videojuegos
    CREATE TABLE IF NOT EXISTS juegos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_juego VARCHAR(255) NOT NULL,
        horas_jugadas INT NOT NULL,
        plataforma VARCHAR(50) NOT NULL,
        porcentaje_progreso INT NOT NULL,
        status VARCHAR(50) NOT NULL
    );

El contenido del archivo **my.cnf** debe tener la siguiente estructura:
    #El servidor MySQL aceptará conexiones desde cualquier dirección IP
    [mysqld]
    bind-address = 0.0.0.0

### Observación
Cuando se conecte a la base de datos de **MySQL**, puede que aparezca el error **"Public Key Retrieval is not allowed"**, puede corregirlo haciendo lo siguiente:
    • **Dbeaver:** Vaya a "Driver properties" en las pestañas superiores de la ventana de conexión, en los drivers selecciona "allowPublicKeyRetrieval" y cambia su parámetro de "false" a "true".