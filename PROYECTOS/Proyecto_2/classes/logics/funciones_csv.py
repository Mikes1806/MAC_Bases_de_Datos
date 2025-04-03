import csv

# Lee un archivo CSV y devuelve los datos como una lista de diccionarios
def leer_csv(table_path):
    with open(table_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Eliminar las comillas simples de los valores
        rows = [{key: value.strip("'") if isinstance(value, str) else value for key, value in row.items()} for row in reader]
        return rows

# Escribe datos en un archivo CSV
def escribir_csv(table_path, data, fieldnames):
    with open(table_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Obtiene las columnas (nombres de campos) de un archivo CSV
def obtener_columnas(table_path):
    with open(table_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames