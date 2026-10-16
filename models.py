from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    nome: Mapped[String] = mapped_column(String(80), nullable=False)
    email: Mapped[String] = mapped_column(String(80), unique=True)
    livros: Mapped[List["Livro"]] = relationship("Livro", back_populates="usuario", lazy='selectin')


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[String] = mapped_column(String(100), nullable=False)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="livros")