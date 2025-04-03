from classes.logics.conexion_bd import DatabaseConnection
from classes.logics.logica_consultas import SQLParser
from classes.logics.ejecucion_consultas import SQLExecutor

class App:
    def __init__(self) -> None:
        self.db_connection = DatabaseConnection()
        self.executor = SQLExecutor(self.db_connection)
        self.parser = SQLParser()

    def run(self):
        # En este espacio realizar las consultas deseadas (+++ = tabla, /// = columna, --- = dato):
            # Sintaxis de CREATE:
            # query = "crear tabla +++ (/// INT,/// VARCHAR,/// VARCHAR,/// INT)"
            # Sintaxis de INSERT
            # query = "insertar en +++ (///,///,///,///) valores (---,'---','---',---)"
            # Sintaxis de SELECT
            # query = "seleccionar * de +++"
            # query = "seleccionar ///,///,///(el mismo) de +++ donde ///(el mismo) = '---'"
            # Sintaxis de UPDATE
            # query = "actualizar +++ asignar /// = '---' donde /// = '---'"
            # Sintaxis de DELETE
            # query = "eliminar de +++ donde /// = ---"
            # Sintaxis de JOIN
            # query = "unir +++(1) con +++(2) donde +++(1).///(1) = +++(2).///(2)"

        try:
            # Parsear la consulta
            parsed_query = self.parser.parse(query)
            
            # Ejecutar la consulta según su tipo
            if parsed_query["type"] == "CREATE":
                result = self.executor.execute_create(parsed_query)
            elif parsed_query["type"] == "SELECT":
                result = self.executor.execute_select(parsed_query)
            elif parsed_query["type"] == "UPDATE":
                result = self.executor.execute_update(parsed_query)
            elif parsed_query["type"] == "INSERT":
                result = self.executor.execute_insert(parsed_query)
            elif parsed_query["type"] == "DELETE":
                result = self.executor.execute_delete(parsed_query)
            elif parsed_query["type"] == "JOIN":
                result = self.executor.execute_join(parsed_query)
            else:
                result = "Tipo de consulta no soportado"
            print(result)
        
        except Exception as e:
            print(f"Error: {e}")

# Ejecutar la aplicación
app = App()
app.run()