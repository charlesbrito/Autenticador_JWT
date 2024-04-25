from sqlalchemy import Boolean, Column, Integer, String
from database import base


# Criação da tabela de usuários
class User(base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)
    hashed_password = Column(String(255))
