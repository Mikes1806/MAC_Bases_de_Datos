import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Login:
    # Constructor para inicializar los valores de username y password
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Conexión a PostgreSQL usando variables de entorno
    def conectar_postgres(self):
        conn = psycopg2.connect(
            dbname = os.getenv("POSTGRES_DB"), 
            user = os.getenv("POSTGRES_USER"), 
            password = os.getenv("POSTGRES_PASSWORD"), 
            host = os.getenv("POSTGRES_HOST"),
            port = "5432"
        )
        return conn

    # Función para verificar login
    def verificar_login(self):
        conn = self.conectar_postgres()  # Usamos self para llamar a conectar_postgres
        cursor = conn.cursor()

        # Consultar la base de datos de PostgreSQL
        query = sql.SQL("SELECT * FROM usuarios WHERE username = %s AND password = %s")
        cursor.execute(query, (self.username, self.password))  # Usamos self.username y self.password
        
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user:
            return True
        else:
            return False