# Usa una imagen base de Python
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /app/

# Instala las dependencias de la aplicación
RUN pip install -r requirements.txt

# Copia el código de la aplicación al directorio de trabajo
COPY . /app/

# Expone el puerto 9200 en el contenedor
EXPOSE 9200

# Comando para ejecutar automáticamente el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:9200"]
