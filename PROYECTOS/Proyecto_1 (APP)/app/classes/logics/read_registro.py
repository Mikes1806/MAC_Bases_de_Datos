import os
import streamlit as st
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Read_registro:
    def __init__(self) -> None:
        pass

    def conectar_mysql(self):
        # Conexión a la base de datos MySQL usando variables de entorno
        try:
            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DB")
            )
            return conn
        except Error as e:
            raise Exception(f"Error al conectar a MySQL: {e}")
    
    def logic(self):
        try:
            # Conexión a MySQL
            connection = self.conectar_mysql()

            if connection.is_connected():
                cursor = connection.cursor()
                # Query para obtener los registros de la tabla
                query = "SELECT * FROM juegos"
                cursor.execute(query)

                # Mostrar los registros en un dataframe
                resultados = cursor.fetchall()

                if resultados:
                    # Muestra los resultados de forma tabular
                    for row in resultados:
                        st.write(f"**ID:** {row[0]}")
                        st.write(f"**Nombre del juego:** {row[1]}")
                        st.write(f"**Horas jugadas:** {row[2]}")
                        st.write(f"**Plataforma:** {row[3]}")
                        st.write(f"**Progreso:** {row[4]}%")
                        st.write(f"**Estado:** {row[5]}")
                        st.write("---")
                else:
                    st.warning("No hay registros disponibles.")
                
        except Exception as e:
            st.error(f"Error al recuperar los registros: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()