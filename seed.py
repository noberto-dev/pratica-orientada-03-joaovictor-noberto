from models import Usuario, Livro
from database import engine
from sqlalchemy.orm import Session

with Session(bind=engine) as session:
    usuario_inicial = Usuario(nome="Maria", email="maria.com@gmail")
    livro_inicial = Livro(titulo="Dom Casmurro", id_usuario=1)

    session.add(usuario_inicial)
    session.add(livro_inicial)

    session.commit()