import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USER = os.environ.get("USER_DATABASE")
PASSWORD = os.environ.get("PASSWORD_DATABASE")
DB_NAME = os.environ.get("NAME_DATABASE")
HOST = os.environ.get("HOST_DATABASE")
PORT = os.environ.get("PORT_DATABASE")

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

try:
    # Intentar conectar al servidor de la base de datos
    with engine.connect() as connection:
        print("Conexión exitosa")
except Exception as e:
    print(f"Error de conexión: {e}")