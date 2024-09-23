from models import Base, Pessoa
from sqlalchemy import VARCHAR, INTEGER
from sqlalchemy.orm import Mapped, mapped_column

class Vinil(Base):
    __tablename__ = "vinil"
    id: Mapped[int] = mapped_column(INTEGER,nullable=False,primary_key=True, autoincrement=True)
    artista: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)
    genero: Mapped[str] = mapped_column(VARCHAR(100), nullable=False)