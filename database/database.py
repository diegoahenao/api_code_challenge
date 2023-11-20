import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

USER = os.environ.get("USER_DATABASE")
PASSWORD = os.environ.get("PASSWORD_DATABASE")
DB_NAME = os.environ.get("NAME_DATABASE")
HOST = os.environ.get("HOST_DATABASE")
PORT = os.environ.get("PORT_DATABASE")

DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()