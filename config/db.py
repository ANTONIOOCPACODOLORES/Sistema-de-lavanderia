from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a MySQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@127.0.0.1:3307/bd_carwash"

# Motor de SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()
 

