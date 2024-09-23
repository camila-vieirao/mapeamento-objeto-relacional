from sqlalchemy.orm import Session
from models import Funcionario

def create_funcionario(session: Session, cpf: str, salario: float):
    try:
        funcionario = Funcionario(cpf=cpf, salario=salario)
        session.add(funcionario)
        session.commit()
        print(f"Funcionário com CPF {cpf} criado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar Funcionário: {e}")

def read_funcionario(session: Session, cpf: str):
    try:
        funcionario = session.query(Funcionario).filter(Funcionario.cpf == cpf).one()
        print(f"Funcionário encontrado: CPF={funcionario.cpf}, Salário={funcionario.salario}")
    except Exception as e:
        print(f"Erro ao ler Funcionário: {e}")

def update_funcionario(session: Session, cpf: str, salario: float = None):
    try:
        funcionario = session.query(Funcionario).filter(Funcionario.cpf == cpf).one()
        if salario is not None:
            funcionario.salario = salario
        session.commit()
        print(f"Funcionário com CPF {cpf} atualizado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar Funcionário: {e}")

def delete_funcionario(session: Session, cpf: str):
    try:
        funcionario = session.query(Funcionario).filter(Funcionario.cpf == cpf).one()
        session.delete(funcionario)
        session.commit()
        print(f"Funcionário com CPF {cpf} deletado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar Funcionário: {e}")
