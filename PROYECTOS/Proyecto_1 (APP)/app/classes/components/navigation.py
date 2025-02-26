import streamlit as st
from streamlit_option_menu import option_menu
from ..logics.welcome import Welcome
from ..logics.create_registro import Create_registro
from ..logics.read_registro import Read_registro
from ..logics.update_registro import Update_registro
from ..logics.delete_registro import Delete_registro

class Navigation:
    def __init__(self) -> None:
        self._init_title = "Bienvenido a MyGames"
        self._menu_handlers = {
            "Inicio": self._handle_Inicio,
            "Mis Juegos": self._handle_Leer_registro,
            "Agregar Juego": self._handle_Crear_registro,
            "Modificar Juego": self._handle_Modificar_registro,
            "Eliminar Juego": self._handle_Eliminar_registro,
            "Cerrar sesión": self.logout,
        }
        self._options = list(self._menu_handlers.keys())

    # Creación del menú lateral de la aplicación
    def render_menu(self) -> None:
        with st.sidebar:
            option = option_menu(
                "Menú",
                self._options,
                icons=[
                    "house",
                    "trophy",
                    "file-plus",
                    "arrow-clockwise",
                    "file-minus",
                    "box-arrow-left",
                ],
                menu_icon="controller",
                default_index=0,
            )
        handler = self._menu_handlers.get(option)
        if handler:
            handler()

    # Se definen las funciones de cada opción del menú lateral
    def _handle_Inicio(self) -> None:
        st.title(self._init_title)
        with st.spinner("Cargando..."):
            Welcome().logic()
    
    def _handle_Leer_registro(self) -> None:
        st.title("Mis Juegos")
        with st.spinner("Cargando..."):
            Read_registro().logic()

    def _handle_Crear_registro(self) -> None:
        st.title("Agregar Juego")
        with st.spinner("Cargando..."):
            Create_registro().logic()

    def _handle_Modificar_registro(self) -> None:
        st.title("Modificar Juego")
        with st.spinner("Cargando..."):
            Update_registro().logic()

    def _handle_Eliminar_registro(self) -> None:
        st.title("Eliminar Juego")
        with st.spinner("Cargando..."):
            Delete_registro().logic()

    def logout(self) -> None:
        st.session_state["logged_in"] = False
        st.rerun()