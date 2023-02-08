from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from urllib.parse import quote
import pyodbc


def connection():
    engine = create_engine('postgresql://postgres:mini667@localhost/component_status')
    conn = engine.connect()
    return conn


def create_session():
    engine = create_engine('postgresql://postgres:mini667@localhost/component_status')
    Session = sessionmaker(bind=engine)
    session_obj = Session()
    return session_obj
