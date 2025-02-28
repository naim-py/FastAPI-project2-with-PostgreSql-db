from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

		   #= 'postgresql://username:password@localhost:port_num/database_name'
URL_DATABASE= 'postgresql://postgres:535268@localhost:5432/QuiseApplication'

engine=create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
