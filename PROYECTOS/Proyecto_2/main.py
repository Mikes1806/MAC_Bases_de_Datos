from classes.logics.conexion_bd import DatabaseConnection
from classes.logics.logica_consultas import SQLParser
from classes.logics.ejecucion_consultas import SQLExecutor

class App:
    def __init__(self) -> None:
        self.db_connection = DatabaseConnection()
        self.executor = SQLExecutor(self.db_connection)
        self.parser = SQLParser()

    def run(self):
        print("Bienvenido al sistema de ejecución de consultas SQL personalizadas.")
        print("Escribe 'salir' para terminar el programa.")
        while True:
            
            query = input(">> ")

            if query.strip().lower() == "salir":
                print("Saliendo del programa.")
                break

            try:
                # Parsear la consulta
                parsed_query = self.parser.parse(query)

                # Ejecutar la consulta según su tipo
                tipo = parsed_query["type"]
                if tipo == "CREATE":
                    result = self.executor.execute_create(parsed_query)
                elif tipo == "SELECT":
                    result = self.executor.execute_select(parsed_query)
                elif tipo == "UPDATE":
                    result = self.executor.execute_update(parsed_query)
                elif tipo == "INSERT":
                    result = self.executor.execute_insert(parsed_query)
                elif tipo == "DELETE":
                    result = self.executor.execute_delete(parsed_query)
                elif tipo == "JOIN":
                    result = self.executor.execute_join(parsed_query)
                else:
                    result = "Tipo de consulta no soportado"

                print(result)

            except Exception as e:
                print(f"Error: {e}")

# Ejecutar la aplicación
app = App()
app.run()