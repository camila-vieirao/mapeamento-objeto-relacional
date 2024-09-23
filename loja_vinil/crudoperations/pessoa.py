from sqlalchemy.orm import Session
from models import Pessoa
from datetime import date

def create_pessoa(session: Session, cpf: str, nome: str, rg: str, data_nasc: date):
    try:
        pessoa = Pessoa(cpf=cpf, nome=nome, rg=rg, data_nasc=data_nasc)
        session.add(pessoa)
        session.commit()
        print(f"Pessoa com CPF {cpf} criada com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar Pessoa: {e}")

def read_pessoa(session: Session, cpf: str):
    try:
        pessoa = session.query(Pessoa).filter(Pessoa.cpf == cpf).one()
        print(f"Pessoa encontrada: CPF={pessoa.cpf}, Nome={pessoa.nome}, RG={pessoa.rg}, Data de Nascimento={pessoa.data_nasc}")
    except Exception as e:
        print(f"Erro ao ler Pessoa: {e}")

def update_pessoa(session: Session, cpf: str, nome: str = None, rg: str = None, data_nasc: date = None):
    try:
        pessoa = session.query(Pessoa).filter(Pessoa.cpf == cpf).one()
        if nome:
            pessoa.nome = nome
        if rg:
            pessoa.rg = rg
        if data_nasc:
            pessoa.data_nasc = data_nasc
        session.commit()
        print(f"Pessoa com CPF {cpf} atualizada com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar Pessoa: {e}")

def delete_pessoa(session: Session, cpf: str):
    try:
        pessoa = session.query(Pessoa).filter(Pessoa.cpf == cpf).one()
        session.delete(pessoa)
        session.commit()
        print(f"Pessoa com CPF {cpf} deletada com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar Pessoa: {e}")
