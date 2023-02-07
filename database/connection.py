from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from urllib.parse import quote
import pyodbc


def connection():
    engine = create_engine('mssql+pyodbc://komponentyuser:%s@a2582m011/komponenty?driver=SQL+Server' % quote("@dient2024"))
    conn = engine.connect()
    return conn


def create_session():
    engine = create_engine('mssql+pyodbc://komponentyuser:%s@a2582m011/komponenty?driver=SQL+Server' % quote("@dient2024"))
    Session = sessionmaker(bind=engine)
    session_obj = Session()
    return session_obj
