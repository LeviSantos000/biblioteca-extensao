from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class TipoContatoModel(Base):
    __tablename__ = "tipo_contato"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(100), nullable=False)

    contatos = relationship("ContatoModel", back_populates="tipo_contato")