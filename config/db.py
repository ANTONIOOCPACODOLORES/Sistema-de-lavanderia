"""
Este archivo permite conectar con la base de datos.
"""
# pylint: disable=invalid-name
from sqlalchemy create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Se recomienda usar el driver explícito (mysql+pymysql)                
SQLALCHEMY_DATABASE_URL = "mysql://root1234@127.0.0.1:3306/sistema-de-lavanderia"    //o lavanderia//

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Se usa PascalCase (SessionLocal) porque es una "fábrica" de sesiones (Clase)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()   

