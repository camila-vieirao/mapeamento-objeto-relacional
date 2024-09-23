from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from urllib.parse import quote

instance = f"mysql+pymysql://root:{quote('1234')}@localhost:3301/tde1"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autoflush=True, autocommit=False)