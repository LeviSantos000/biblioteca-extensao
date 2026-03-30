from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class EnderecoModel(Base):
    __tablename__ = "endereco"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(150), nullable=True)
    numero = Column(String(20), nullable=True)
    complemento = Column(String(100), nullable=True)
    cep = Column(String(20), nullable=True)
    cidade = Column(String(100), nullable=True)
    estado = Column(String(50), nullable=True)
    id_bairro = Column(Integer, nullable=True)

    usuarios = relationship("UsuarioModel", back_populates="endereco")