import os
import streamlit as st
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar las variables de entorno del archivo .env
load_dotenv()

class Delete_registro:
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
        # Pedir el ID del juego a eliminar
        id_juego = st.number_input("ID del juego a eliminar", min_value=1)
        
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
                        # Mostrar los detalles del juego antes de eliminarlo
                        st.write(f"**Nombre del juego:** {juego[1]}")
                        st.write(f"**Horas jugadas:** {juego[2]}")
                        st.write(f"**Plataforma:** {juego[3]}")
                        st.write(f"**Progreso:** {juego[4]}%")
                        st.write(f"**Estado:** {juego[5]}")

                        if st.button("Eliminar"):
                            # Query de eliminación
                            delete_query = "DELETE FROM juegos WHERE id = %s"
                            cursor.execute(delete_query, (id_juego,))
                            connection.commit()
                            st.success(f"¡Registro con ID {id_juego} eliminado exitosamente!")
                    else:
                        st.warning(f"No se encontró un juego con ID {id_juego}")

            except Exception as e:
                st.error(f"Error al eliminar el registro: {e}")

            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()