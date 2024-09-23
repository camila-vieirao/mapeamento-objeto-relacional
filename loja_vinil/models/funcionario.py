from models import Base, Pessoa
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, DECIMAL, ForeignKey, CHAR

class Funcionario(Base):
    __tablename__ = "funcionario"
    cpf: Mapped[int] = mapped_column(CHAR(11), ForeignKey(Pessoa.cpf), primary_key=True, nullable=False)
    salario: Mapped[float] = mapped_column(DECIMAL(8,2), nullable=False)

    