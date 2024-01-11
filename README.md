# SAEBE
Backend del Sistema de gestíón de Auxiliares de Enseñanza

# Requerimientos
Para poder configurar este proyecto necesitas:
- Python 3+
- Postgres 14
- Django y DjangoRestFramework


## Instalación de dependencias
Para instalar las dependencias del proyecto, siga estos pasos:
1. Instalar Pip:
- Descarga el archivo get-pip.py desde el siguiente enlace: get-pip.py
- Guarda el archivo get-pip.py en una ubicación de tu elección en tu computadora.
- Abre una ventana de línea de comandos (Command Prompt) y navega hasta la ubicación donde guardaste el archivo get-pip.py.
- Ejecuta el siguiente comando para instalar Pip:
    `python get-pip.py`
- Verifica la instalación ejecutando pip --version en la línea de comandos. Deberías ver la versión de Pip instalada en tu sistema.
2. Instalar Virtualenv:
- Abre una ventana de línea de comandos (Command Prompt).
- Ejecuta el siguiente comando para instalar Virtualenv utilizando Pip:
    `pip install virtualenv`
- Verifica la instalación ejecutando virtualenv --version en la línea de comandos. Deberías ver la versión de Virtualenv instalada en tu sistema.

3. Creamos el entorno virtual:
    `python -m venv venv`

4. Active el virtualenv del proyecto.
    `.\venv\Scripts\activate `

5. Actualizar pip
    `python.exe -m pip install --upgrade pip`

- Abra una terminal dentro del proyecto, en la misma ubicación que el archivo *instalaciones_requeridas.txt*


6. Ejecute el siguiente comando pip para instalar las dependencias del proyecto desde el archivo *instalaciones_requeridas.txt*:
`pip install -r requirements.txt`

## Correr migraciones
Para crear la base de datos localmente deben correr el siguiente comando
`python .\manage.py makemigrations`
`python .\manage.py migrate`

## Correr backend
Una vez migrado, hacer
`python .\manage.py runserver`
