import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    # Cadena de conexión a la base de datos desde el archivo .env
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://root:@localhost:3306/ong')  # Valor por defecto
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Clave secreta desde el archivo .env
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')  # Valor por defecto
