import streamlit as st
from classes.components.login import Login
from classes.components.navigation import Navigation

class App:
    def show_page(self):
        obj_navigation = Navigation()
        obj_navigation.render_menu()

    def run(self):
        if "logged_in" not in st.session_state:
            st.session_state["logged_in"] = False
        if st.session_state.logged_in:
            self.show_page()
        else:
            st.title("MyGames")
            username = st.text_input("Nombre de usuario")
            password = st.text_input("Contraseña", type="password")
            if st.button("Iniciar sesión"):
                # Verifica que el nombre de usuario y la contraseña no estén vacíos
                if username and password:
                    try:
                        # Crear un objeto Login pasando los parámetros de usuario y contraseña
                        obj_login = Login(username, password)
                        # Llamar al método verificar_login para validar las credenciales
                        if obj_login.verificar_login():
                            st.session_state["logged_in"] = True
                            st.rerun()
                        else:
                            st.error("Nombre de usuario o contraseña incorrectos.")
                    except TypeError as e:
                        st.error(f"Error al crear el objeto Login: {e}")
                else:
                    st.error("Por favor, ingrese nombre de usuario y contraseña.")

# Ejecutar la aplicación
app = App()
app.run()