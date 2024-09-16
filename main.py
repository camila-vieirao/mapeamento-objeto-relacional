from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base, Discente, Responsavel

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Operações de exemplo
def create_responsavel(db: Session, cpf: str, nome: str, endereco: str, contato_email: str, contato_telefone: str, tipo_tutor: str):
    db_responsavel = Responsavel(cpf=cpf, id_pessoa=cpf, tipo_tutor=tipo_tutor)
    db.add(db_responsavel)
    db.commit()
    db.refresh(db_responsavel)
    return db_responsavel

def create_discente(db: Session, nome: str, genero: str, data_nasc: str, idade: int, cpf: str, data_matric: str, responsavel_cpf: str):
    # Converte as strings de data em objetos datetime.date
    data_nasc = datetime.strptime(data_nasc, '%Y-%m-%d').date()
    data_matric = datetime.strptime(data_matric, '%Y-%m-%d').date()

    db_discente = Discente(nome=nome, genero=genero, data_nasc=data_nasc, idade=idade, cpf=cpf, data_matric=data_matric, responsavel_id=responsavel_cpf)
    db.add(db_discente)
    db.commit()
    db.refresh(db_discente)
    return db_discente

def main():
    db = next(get_db())
    # Criação de um responsável primeiro
    create_responsavel(db, "12345678900", "Maria Silva", "Rua Exemplo, 123", "maria@email.com", "123456789", "Mãe")
    
    # Agora, cria um discente associado ao responsável
    new_discente = create_discente(db, "João Silva", "M", "2005-03-15", 19, "12345678900", "2024-01-01", "12345678900")
    print(f"Discente criado: {new_discente.nome}")

if __name__ == "__main__":
    main()
