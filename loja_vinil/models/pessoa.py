from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import INTEGER, CHAR, DATE, VARCHAR
from datetime import date

class Pessoa(Base):
    __tablename__ = "pessoa"
    
    cpf: Mapped[str] = mapped_column(CHAR(11), nullable=False, primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column("pessoa_nome", VARCHAR(256), nullable=False)
    rg: Mapped[str] = mapped_column(VARCHAR(12), nullable=False, unique=True)
    data_nasc: Mapped[date] = mapped_column(DATE, nullable=False)

    # Relacionamento com Cliente, resolvido via string para evitar problemas de circularidade
    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="pessoa", uselist=False)
