from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# config
SQLALCHEMY_DB_URL = 'sqlite:///app/data/base.db'
MYSQL_DB_URL = ''

Base = declarative_base()
engin = create_engine(SQLALCHEMY_DB_URL)
Session = sessionmaker(bind=engin)

# model to dict
def to_dict(self):
    return {c.name: getattr(self, c.name, None)
            for c in self.__table__.columns}
Base.to_dict = to_dict
