# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import sessionmaker, Session
# from app.models import *
#
# engine = create_engine(url='mysql+pymysql://root:21805Sasha_@localhost/school')
#
# metadata = MetaData(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

session_factory = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind = create_engine('mysql+pymysql://root:21805Sasha_@localhost/school', echo = True)
))


