from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db")

def nova_sessao():
    return Session(bind=engine)