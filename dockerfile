# Usa una imagen de base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo Python al contenedor
COPY fibonacci.py .

# Comando para ejecutar el script
CMD ["python", "fibonacci.py"]
