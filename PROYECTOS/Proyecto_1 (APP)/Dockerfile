# Usar una versión estable de Python
FROM python:3.11

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Configuraciones para evitar archivos bytecode de Python y mantener logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copiar y instalar dependencias antes de copiar todo el código (mejora la caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Comando por defecto para ejecutar la app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]