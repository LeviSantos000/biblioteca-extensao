from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class ContatoModel(Base):
    __tablename__ = "contato"

    id = Column(Integer, primary_key=True, autoincrement=True)
    contato = Column(String(150), nullable=False)
    status = Column(Boolean, default=True, nullable=False)
    id_tipo_contato = Column(Integer, ForeignKey("tipo_contato.id"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)

    tipo_contato = relationship("TipoContatoModel", back_populates="contatos")
    usuario = relationship("UsuarioModel", back_populates="contatos")