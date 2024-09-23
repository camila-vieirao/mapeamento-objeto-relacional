from sqlalchemy.orm import Session
from models import Vinil

def create_vinil(session: Session, id: int, artista: str, genero: str):
    try:
        vinil = Vinil(id=id, artista=artista, genero=genero)
        session.add(vinil)
        session.commit()
        print(f"Vinil com ID {id} criado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar Vinil: {e}")

def read_vinil(session: Session, id: int):
    try:
        vinil = session.query(Vinil).filter(Vinil.id == id).one()
        print(f"Vinil encontrado: ID={vinil.id}, Artista={vinil.artista}, Gênero={vinil.genero}")
    except Exception as e:
        print(f"Erro ao ler Vinil: {e}")

def update_vinil(session: Session, id: int, artista: str = None, genero: str = None):
    try:
        vinil = session.query(Vinil).filter(Vinil.id == id).one()
        if artista:
            vinil.artista = artista
        if genero:
            vinil.genero = genero
        session.commit()
        print(f"Vinil com ID {id} atualizado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao atualizar Vinil: {e}")

def delete_vinil(session: Session, id: int):
    try:
        vinil = session.query(Vinil).filter(Vinil.id == id).one()
        session.delete(vinil)
        session.commit()
        print(f"Vinil com ID {id} deletado com sucesso!")
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar Vinil: {e}")
