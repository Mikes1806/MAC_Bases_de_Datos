import os
import streamlit as st
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Update_registro:
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
        # Pedir el ID del juego a modificar
        id_juego = st.number_input("ID del juego a modificar", min_value=1)
        
        if id_juego:
            try:
                # Conexión a MySQL
                connection = self.conectar_mysql()

                if connection.is_connected():
                    cursor = connection.cursor()
                    # Query para obtener el registro por ID
                    query = "SELECT * FROM juegos WHERE id = %s"
                    cursor.execute(query, (id_juego,))
                    juego = cursor.fetchone()

                    if juego:
                        # Mostrar los valores actuales para que el usuario pueda modificarlos
                        nombre_juego = st.text_input("Nombre del videojuego", value=juego[1])
                        horas_jugadas = st.number_input("Horas jugadas", min_value=0, value=juego[2])
                        plataforma = st.selectbox("Plataforma", ["PlayStation", "Xbox", "Nintendo", "PC", "Otro"], index=["PlayStation", "Xbox", "Nintendo", "PC", "Otro"].index(juego[3]))
                        porcentaje_progreso = st.slider("Porcentaje de progreso", 0, 100, value=juego[4])
                        status = st.selectbox("Estado", ["En pausa", "En progreso", "Terminado", "Platino"], index=["En pausa", "En progreso", "Terminado", "Platino"].index(juego[5]))

                        if st.button("Modificar"):
                            # Query de actualización
                            update_query = """
                            UPDATE juegos
                            SET nombre_juego = %s, horas_jugadas = %s, plataforma = %s, porcentaje_progreso = %s, status = %s
                            WHERE id = %s
                            """
                            cursor.execute(update_query, (nombre_juego, horas_jugadas, plataforma, porcentaje_progreso, status, id_juego))
                            connection.commit()
                            st.success(f"¡Registro con ID {id_juego} modificado exitosamente!")

                    else:
                        st.warning(f"No se encontró un juego con ID {id_juego}")

            except Exception as e:
                st.error(f"Error al modificar el registro: {e}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()