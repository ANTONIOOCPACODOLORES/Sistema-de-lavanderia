from sqlalchemy import column
from sqlalchemy.orm
fromc config

class User(Base):
    __tablename__ = 'the_users'
    id = Column(Integer, primary_key=True, index=True)
    rol_id = Column(Integer, ForeignKey('the_rols.id'))

    