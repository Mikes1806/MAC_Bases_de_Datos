# Proyecto 4

## Descripción
• El proyecto está estructurado como un mini Data Warehouse (modelo estrella), simulando una arquitectura tipo Data Lake con tres capas de datos: **Bronze**, **Silver** y **Gold**, las cuales representan: datos crudos, datos limpios y datos analíticos, respectivamente.
• El modelo incluye una tabla de hechos **Ventas** y tres tablas de dimensiones: **Fecha**, **Producto** y **Tienda**.  
• Los datos son generados de forma sintética utilizando la biblioteca **Faker** y manipulados con **Pandas**.

## Características
• Generación automatizada de datasets sintéticos realistas con **Faker**.  
• Construcción de una base de datos en forma de estrella para análisis de ventas.  
• Uso de **Pandas** para limpieza, transformación y consultas sobre los datos.  
• Consultas clave sobre la tabla de hechos **Ventas** para obtener información de valor.

## Arquitectura de Datos
• Este proyecto simula un flujo de procesamiento tipo **Data Lakehouse**, dividido en tres capas de datos:
1. **Bronze**: Contiene los datos generados crudos directamente con **Faker**, sin transformación.
2. **Silver**: Datos limpios y normalizados utilizando **Pandas** (por ejemplo: eliminación de duplicados).
3. **Gold**: Datos listos para análisis, como las tablas del modelo estrella y las vistas o DataFrames generados a partir de consultas agregadas.
• Este enfoque permite aplicar buenas prácticas de arquitectura analítica en un entorno simulado con Python y archivos 
**.csv**, emulando una implementación de **Data Warehouse** sobre un **Data Lake**.

## Requisitos
• Python 3.10 (en adelante).
• Bibliotecas estándar de Python:
   - os: para manejo del sistema de archivos.
   - random: para generación aleatoria de datos.
• Bibliotecas externas necesarias:
   - faker: para generación de datos sintéticos (nombres, fechas, productos, etc.).
   - pandas: para manipulación, transformación y análisis de datos.
   - numpy: para operaciones numéricas.
   - pyarrow: para guardar datos en formato Parquet si se simulan capas tipo Bronze, Silver y Gold.

## Instrucciones de Uso
1. Clona el repositorio:
    git clone https://github.com/Mikes1806/MAC_Bases_de_Datos.git
2. Ejecuta el notebook **ventas.ipynb** celda por celda para ver el proceso del **Data Lakehouse**.