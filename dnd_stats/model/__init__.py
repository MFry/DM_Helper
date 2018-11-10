from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite://')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

from .characters import Characters
#from .fight_stats import