from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from database import Base

class Pessoa(Base):
    __tablename__ = 'pessoa'
    
    cpf = Column(String, primary_key=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    contato_email = Column(String(255), nullable=False)
    contato_telefone = Column(String(15), nullable=True)

class Discente(Base):
    __tablename__ = 'discente'
    
    ra = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    genero = Column(String(1), nullable=False)
    data_nasc = Column(Date, nullable=False)
    idade = Column(Integer, nullable=True)
    cpf = Column(String(11), ForeignKey('pessoa.cpf'), unique=True, nullable=False)
    data_matric = Column(Date, nullable=False)

    responsavel_id = Column(String, ForeignKey('responsavel.cpf'), nullable=False)  # Corrigido para String
    responsavel = relationship("Responsavel", back_populates="discentes")

class Responsavel(Base):
    __tablename__ = 'responsavel'

    cpf = Column(String, primary_key=True)
    id_pessoa = Column(String, ForeignKey('pessoa.cpf'))  # Corrigido para String
    tipo_tutor = Column(String(50), nullable=False)

    discentes = relationship("Discente", back_populates="responsavel")

class Funcionario(Base):
    __tablename__ = 'funcionario'

    codigo_rh = Column(Integer, primary_key=True)
    id_pessoa = Column(String, ForeignKey('pessoa.cpf'))  # Corrigido para String
    genero = Column(String(1), nullable=False)
    data_nasc = Column(Date, nullable=False)
    data_inicio = Column(Date, nullable=False)

class Docente(Funcionario):
    __tablename__ = 'docente'

    codigo_rh = Column(String, primary_key=True)
    id_pessoa = Column(String, ForeignKey('pessoa.cpf'))
    __mapper_args__ = {
        'inherit_condition': Funcionario.codigo_rh == Funcionario.codigo_rh  # Utilize a referência correta
    }

class Cargo(Base):
    __tablename__ = 'cargo'
    
    id_cargo = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    salario = Column(DECIMAL(8, 2), nullable=False)

class Setor(Base):
    __tablename__ = 'setor'
    
    id_setor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String, nullable=True)

class Disciplina(Base):
    __tablename__ = 'disciplina'
    
    id_disciplina = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    carga_horaria = Column(Integer, nullable=False)

class Avaliacao(Base):
    __tablename__ = 'avaliacao'
    
    id_avaliacao = Column(Integer, primary_key=True, autoincrement=True)
    nota = Column(DECIMAL(5, 2), nullable=False)
    bimestre = Column(Integer, nullable=False)

class Turma(Base):
    __tablename__ = 'turma'
    
    id_turma = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    serie = Column(Integer, nullable=False)
    nome = Column(String(255))

class Sala(Base):
    __tablename__ = 'sala'
    
    id_sala = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    nome = Column(String(255), nullable=False)
    capacidade = Column(Integer, nullable=False)
    bloco = Column(String(255), nullable=False)
    bloco_andar = Column(Integer, nullable=False)

class Mensalidade(Base):
    __tablename__ = 'mensalidade'
    
    id_mensalidade = Column(Integer, primary_key=True, autoincrement=True)
    valor_total = Column(DECIMAL(8, 2), nullable=False)

class Parcela(Base):
    __tablename__ = 'parcela'
    
    id_parcela = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    status = Column(Enum('pago', 'pendente', 'atrasado'), nullable=False)
    data_vencimento = Column(Date, nullable=False)
    valor = Column(DECIMAL(8, 2), nullable=False)
