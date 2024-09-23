from sqlalchemy.orm import Session
from models import Cliente, Pessoa


def create_cliente(session: Session, cpf: str, endereco: str):
    try:
        pessoa_exists = session.query(Pessoa).filter(Pessoa.cpf == cpf).one_or_none()
        if not pessoa_exists:
            print(f"Erro: CPF {cpf} não encontrado na tabela Pessoa.")
            return

        cliente = Cliente(cpf=cpf, endereco=endereco)
        session.add(cliente)
        session.commit()
        print(f"Cliente com CPF {cpf} criado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar Cliente: {e}")

def read_cliente(session: Session, cpf: str):
    try:
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).one()
        print(f"Cliente encontrado: CPF={cliente.cpf}, Endereço={cliente.endereco}")
    except Exception as e:
        print(f"Erro ao ler Cliente: {e}")

def update_cliente(session: Session, cpf: str, endereco: str = None):
    try:
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).one()
        if endereco:
            cliente.endereco = endereco
        session.commit()
        print(f"Cliente com CPF {cpf} atualizado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar Cliente: {e}")

def delete_cliente(session: Session, cpf: str):
    try:
        cliente = session.query(Cliente).filter(Cliente.cpf == cpf).one()
        session.delete(cliente)
        session.commit()
        print(f"Cliente com CPF {cpf} deletado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar Cliente: {e}")