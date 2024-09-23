from models import Base, Pessoa
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, CHAR, ForeignKey, VARCHAR

class Cliente(Base):
    __tablename__ = "cliente"
    cpf: Mapped[int] = mapped_column(CHAR(11), ForeignKey(Pessoa.cpf), primary_key=True, nullable=False)
    endereco: Mapped[str] = mapped_column(VARCHAR(256), nullable=False, unique=True)
    
    pessoa: Mapped["Pessoa"] = relationship("Pessoa", back_populates="cliente")
