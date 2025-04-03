import re

class SQLParser:
    
    # Parsea la consulta en español
    def parse(self, query):
        query = query.strip().lower()
        if query.startswith("seleccionar"):
            return self.parse_select(query)
        elif query.startswith("insertar"):
            return self.parse_insert(query)
        elif query.startswith("actualizar"):
            return self.parse_update(query)
        elif query.startswith("eliminar"):
            return self.parse_delete(query)
        elif query.startswith("unir"):
            return self.parse_join(query)
        elif query.startswith("crear"):
            return self.parse_create(query)
        else:
            raise ValueError("Consulta no soportada")

    # Parsea un CREATE TABLE
    def parse_create(self, query):
        match = re.match(r"crear tabla (\w+) \((.+)\)", query)
        if not match:
            raise ValueError("Sintaxis de CREATE incorrecta")
        tabla, columnas = match.groups()
        columnas = columnas.split(",")
        columnas = [col.strip().split(" ")[0] for col in columnas]  # Solo tomamos el nombre de la columna
        return {"type": "CREATE", "table": tabla.strip(), "columns": columnas}

    # Parsea un SELECT
    def parse_select(self, query):
        # Se condiciona si es que existe el WHERE
        match = re.match(r"seleccionar (.+) de (\w+)( donde (.+))?", query)
        
        if not match:
            raise ValueError("Sintaxis de SELECT incorrecta")
        columnas, tabla, _, where_clause = match.groups()
        columnas = columnas.split(",")

        # Si existe el WHERE, se ejecuta
        where = None
        if where_clause:
            where = where_clause.strip()

        return {"type": "SELECT", "columns": columnas, "table": tabla.strip(), "where": where}

    # Parsea un INSERT
    def parse_insert(self, query):
        match = re.match(r"insertar en (\w+) \((.+)\) valores \((.+)\)", query)
        if not match:
            raise ValueError("Sintaxis de INSERT incorrecta")
        tabla, columnas, valores = match.groups()
        return {"type": "INSERT", "table": tabla.strip(), "columns": columnas.split(","), "values": valores.split(",")}
    
    # Parsea un UPDATE
    def parse_update(self, query):
        match = re.match(r"actualizar (\w+) asignar (.+) donde (.+)", query)
        if not match:
            raise ValueError("Sintaxis de UPDATE incorrecta")
        tabla, set_clause, where_clause = match.groups()
        return {"type": "UPDATE", "table": tabla.strip(), "set": set_clause.strip(), "where": where_clause.strip()}

    # Parsea un DELETE
    def parse_delete(self, query):
        match = re.match(r"eliminar de (\w+) donde (.+)", query)
        if not match:
            raise ValueError("Sintaxis de DELETE incorrecta")
        tabla, where_clause = match.groups()
        return {"type": "DELETE", "table": tabla.strip(), "where": where_clause.strip()}

    # Parsea un JOIN
    def parse_join(self, query):
        match = re.match(r"unir (\w+) con (\w+) donde (\w+\.\w+) = (\w+\.\w+)", query)
        if not match:
            raise ValueError("Sintaxis de JOIN incorrecta")
        tabla1, tabla2, columna1, columna2 = match.groups()
        return {
            "type": "JOIN",
            "table1": tabla1.strip(),
            "table2": tabla2.strip(),
            "columna1": columna1.strip(),
            "columna2": columna2.strip()
        }