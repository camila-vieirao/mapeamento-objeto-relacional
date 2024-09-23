from services.database import engine
from models import *

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)