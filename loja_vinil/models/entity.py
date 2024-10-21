from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CHAR, VARCHAR, DATE, INTEGER, DECIMAL, ForeignKey
from datetime import date
from .base import Base

# Pessoa Model
class Pessoa(Base):
    __tablename__ = "pessoa"
    
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column("pessoa_nome", VARCHAR(256), nullable=False)
    rg: Mapped[str] = mapped_column(VARCHAR(12), nullable=False, unique=True)
    data_nasc: Mapped[date] = mapped_column(DATE, nullable=False)

    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="pessoa", uselist=False)

# Cliente Model
class Cliente(Base):
    __tablename__ = "cliente"
    cpf: Mapped[int] = mapped_column(CHAR(11), ForeignKey(Pessoa.cpf), primary_key=True, nullable=False)
    endereco: Mapped[str] = mapped_column(VARCHAR(256), nullable=False, unique=True)
    
    pessoa: Mapped["Pessoa"] = relationship("Pessoa", back_populates="cliente")

# Funcionario Model
class Funcionario(Base):
    __tablename__ = "funcionario"
    cpf: Mapped[int] = mapped_column(CHAR(11), ForeignKey(Pessoa.cpf), primary_key=True, nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(8, 2), nullable=False)

# Vinil Model
class Vinil(Base):
    __tablename__ = "vinil"
    id: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    artista: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    genero: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
