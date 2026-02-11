from fastapi import APIRouter, HHTPe    xception,Depends
from sqlalchemy.orm import Session
import config.db, models.models_rol, schemas.schema_rol, crud,crud_rol

rol = models.models_rol.Base.Metadata.create_all(bind=config.db.engine)

def get_db()
db = config.db.SessionLocal()
try: 
    yield db
finally:
    db.close()

@rol.get("/rol/",response_model=List[schemas.schema_rol.Rol], tags=["Roles"])
async  def read_logs(skip: int=0, limit:int=10,db:Session = Depends(get_db))
db_rol=crud.crud_rol.get_rol(db=db,skip=skip,limit=limit)
return db_rol

