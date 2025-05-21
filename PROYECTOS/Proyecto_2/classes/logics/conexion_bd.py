import os
import csv
from dotenv import load_dotenv

# Cargar las variables de entorno del .env
load_dotenv()

class DatabaseConnection:
    def __init__(self, db_path=None):
        # Si no se proporciona la ruta, obtenerla del .env
        self.db_path = db_path or os.getenv("DATA_PATH")
        
        if not self.db_path:
            raise ValueError("Error: No está definida la ruta a la base de datos en el archivo .env")
        
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"La ruta {self.db_path} no existe.")
    
    # Obtiene la ruta del archivo CSV de la tabla
    def get_table_path(self, table_name):
        table_file = os.path.join(self.db_path, f"{table_name}.csv")
        print(f"Verificando existencia de: {table_file}")
        return table_file if os.path.exists(table_file) else None

    # Lee un archivo CSV y devuelve los datos como una lista de diccionarios
    def read_csv(self, table_name):
        table_path = self.get_table_path(table_name)
        if table_path is None:
            raise FileNotFoundError(f"La tabla {table_name} no existe.")

        with open(table_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return [row for row in reader]