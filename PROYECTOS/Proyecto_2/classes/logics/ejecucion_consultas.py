import os
from classes.logics.funciones_csv import escribir_csv, leer_csv

class SQLExecutor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Crea un archivo CSV con las columnas especificadas
    def _crear_tabla(self, tabla, columnas):
        table_path = self.db_connection.get_table_path(tabla)
        
        if table_path and os.path.exists(table_path):
            raise FileExistsError(f"La tabla {tabla} ya existe.")
        
        # Crear la ruta manualmente si no existe
        table_path = os.path.join(self.db_connection.db_path, f"{tabla}.csv")
        
        # Crea un archivo CSV vacío con los encabezados de las columnas
        escribir_csv(table_path, [], columnas)
        return f"Tabla {tabla} creada con éxito."
    
    # Lee un archivo CSV con las columnas especificadas
    def _leer_tabla(self, tabla, columnas):
        table_path = self.db_connection.get_table_path(tabla)
        
        if not table_path or not os.path.exists(table_path):
            raise FileNotFoundError(f"La tabla {tabla} no existe.")
        
        datos = leer_csv(table_path)
        columnas_disponibles = datos[0].keys() if datos else []
        
        # Asegurar que WHERE funcione, incluyendo todas las columnas aunque no se seleccionen
        datos_procesados = [
            {col.strip(): row[col].strip() for col in columnas_disponibles} for row in datos
        ]
        
        # Si el usuario pidió "*", devolvemos todo
        if columnas == ["*"]:
            return datos_procesados

        # Filtrar solo las columnas deseadas, pero manteniendo las del WHERE
        resultado = [
            {col: fila[col] for col in columnas if col in fila} for fila in datos_procesados
        ]
        
        return resultado

    # Ejecuta CREATE TABLE
    def execute_create(self, parsed_query):
        tabla = parsed_query["table"]
        columnas = parsed_query["columns"]
        return self._crear_tabla(tabla, columnas)
    
    # Ejecuta SELECT
    def execute_select(self, parsed_query):
        if parsed_query["type"] == "SELECT":
            pass

        # Lee la tabla
        datos = self._leer_tabla(parsed_query["table"], parsed_query["columns"])

        # Si hay un WHERE, se aplica
        where = parsed_query.get("where")
        result = datos

        if where:
            try:
                # Intentar separar por =
                partes_where = where.split("=")
                
                if len(partes_where) != 2:
                    raise ValueError(f"Condición WHERE mal formada: {where}")

                columna, valor = partes_where
                columna = columna.strip()
                valor = valor.strip().strip("'")  # Eliminar comillas si las tiene

                # Verificar si la columna existe en los datos
                if not datos or columna not in datos[0]:
                    raise ValueError(f"La columna '{columna}' no existe en la tabla.")

                # Filtrar datos
                result = [row for row in result if row.get(columna) == str(valor)]
            except Exception:
                pass
        
        return f"Su consulta: {result}"

    # Ejecuta INSERT
    def execute_insert(self, parsed_query):
        tabla = parsed_query["table"]
        columnas = parsed_query["columns"]
        valores = parsed_query["values"]
        
        table_path = self.db_connection.get_table_path(tabla)
        
        if not table_path or not os.path.exists(table_path):
            raise FileNotFoundError(f"La tabla {tabla} no existe.")
        
        datos = leer_csv(table_path)
        nueva_fila = dict(zip(columnas, valores))
        datos.append(nueva_fila)
        escribir_csv(table_path, datos, columnas)
        return f"Datos insertados en la tabla {tabla}: {nueva_fila}"

    # Ejecuta UPDATE
    def execute_update(self, parsed_query):
        tabla = parsed_query["table"]
        set_clause = parsed_query["set"]
        where_clause = parsed_query["where"]

        table_path = self.db_connection.get_table_path(tabla)
        
        if not table_path or not os.path.exists(table_path):
            raise FileNotFoundError(f"La tabla {tabla} no existe.")
        
        datos = leer_csv(table_path)
        set_values = {col.split('=')[0].strip(): col.split('=')[1].strip() for col in set_clause.split(',')}
        columna_where, valor_where = where_clause.split("=")
        columna_where = columna_where.strip()
        valor_where = valor_where.strip().strip("'")

        for row in datos:
            if row[columna_where] == valor_where:
                for col, val in set_values.items():
                    row[col] = val.strip().strip("'")

        escribir_csv(table_path, datos, datos[0].keys())
        return f"Datos actualizados en la tabla {tabla} donde {columna_where} = {valor_where}"
    
    # Ejecuta DELETE
    def execute_delete(self, parsed_query):
        tabla = parsed_query["table"]
        where_clause = parsed_query["where"]

        # Obtener la ruta del CSV
        table_path = self.db_connection.get_table_path(tabla)
        
        if not table_path or not os.path.exists(table_path):
            raise FileNotFoundError(f"La tabla {tabla} no existe.")
        
        # Lee los datos de la tabla
        datos = leer_csv(table_path)
        
        # Parsear el WHERE
        columna_where, valor_where = where_clause.split("=")
        columna_where = columna_where.strip()
        valor_where = valor_where.strip().strip("'")
        
        # Eliminar las filas que cumplen con el WHERE
        datos_filtrados = [row for row in datos if row[columna_where] != valor_where]
        
        # Escribir los datos actualizados (sin las filas eliminadas)
        escribir_csv(table_path, datos_filtrados, datos[0].keys())
        
        return f"Datos eliminados en la tabla {tabla} donde {columna_where} = {valor_where}"

    # Ejecuta JOIN
    def execute_join(self, parsed_query):
        tabla1 = parsed_query["table1"]
        tabla2 = parsed_query["table2"]
        columna1 = parsed_query["columna1"]
        columna2 = parsed_query["columna2"]
        return self._realizar_join(tabla1, tabla2, columna1, columna2)

    # Realiza el JOIN entre dos tablas, basándose en las columnas especificadas
    def _realizar_join(self, tabla1, tabla2, columna1, columna2):
        table_path1 = self.db_connection.get_table_path(tabla1)
        table_path2 = self.db_connection.get_table_path(tabla2)
        
        if not table_path1 or not os.path.exists(table_path1):
            raise FileNotFoundError(f"La tabla {tabla1} no existe.")
        if not table_path2 or not os.path.exists(table_path2):
            raise FileNotFoundError(f"La tabla {tabla2} no existe.")
        
        # Lee ambas tablas
        datos1 = leer_csv(table_path1)
        datos2 = leer_csv(table_path2)

        # Obtiene el nombre de las columnas
        columnas1 = datos1[0].keys() if datos1 else []
        columnas2 = datos2[0].keys() if datos2 else []

        # Hace el JOIN basado en la columna correspondiente
        columna1_name = columna1.split(".")[1]
        columna2_name = columna2.split(".")[1]

        resultado = []
        for row1 in datos1:
            for row2 in datos2:
                if row1[columna1_name] == row2[columna2_name]:
                    # Unir las filas de ambas tablas
                    resultado_fila = {**row1, **row2}
                    resultado.append(resultado_fila)

        return f"Su consulta: {resultado}"