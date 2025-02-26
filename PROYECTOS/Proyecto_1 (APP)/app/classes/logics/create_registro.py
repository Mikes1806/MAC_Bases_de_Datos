import os
import streamlit as st
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Create_registro:
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

    def logic(self) -> None:
        # Pedir datos al usuario
        nombre_juego = st.text_input("Nombre del videojuego")
        horas_jugadas = st.number_input("Horas jugadas", min_value=0)
        plataforma = st.selectbox("Plataforma", ["PlayStation", "Xbox", "Nintendo", "PC", "Otro"])
        porcentaje_progreso = st.slider("Porcentaje de progreso", 0, 100, 0)
        status = st.selectbox("Estado", ["En pausa", "En progreso", "Terminado", "Platino"])

        if st.button("Guardar"):
            # Validación de los datos
            if nombre_juego and horas_jugadas >= 0:
                try:
                    # Conexión a MySQL
                    connection = self.conectar_mysql()

                    if connection.is_connected():
                        cursor = connection.cursor()
                        # Query de inserción en la tabla
                        query = """
                        INSERT INTO juegos (nombre_juego, horas_jugadas, plataforma, porcentaje_progreso, status)
                        VALUES (%s, %s, %s, %s, %s)
                        """
                        # Ejecución de la query con los datos del formulario
                        cursor.execute(query, (nombre_juego, horas_jugadas, plataforma, porcentaje_progreso, status))

                        # Confirmación de la operación
                        connection.commit()

                        st.success("¡Juego registrado exitosamente!")

                except Exception as e:
                    st.error(f"Error al procesar la solicitud: {e}")

                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

            else:
                st.error("Por favor, completa todos los campos.")