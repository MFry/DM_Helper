from sqlalchemy import Column, Integer, String
from model import Base


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    dnd_class = Column('class', String)
    dnd_subclass = Column('subclass', String)
