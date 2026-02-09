#esta clase representa la clase rol del usuario//
from sqlalchemy import column, Integer, String, boolean
from config import Base
from sqlalchemy.orm import relationship

class Rol(Base):
    #en este apartado se define  la clase con sus atributos//
    __tablename__='tbc_roles'
    
    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String(60))
    estatus = Column(boolean,default=True)

    usuario=relationship("User", back_populates="rol")
