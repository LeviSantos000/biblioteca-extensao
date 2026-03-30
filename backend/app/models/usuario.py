from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=True)
    data_nascimento = Column(Date, nullable=True)
    cpf = Column(String(14), unique=True, nullable=False)
    sexo = Column(String(1), nullable=True)
    status = Column(Boolean, default=True, nullable=False)
    id_endereco = Column(Integer, ForeignKey("endereco.id"), nullable=True)

    endereco = relationship("EnderecoModel", back_populates="usuarios")
    contatos = relationship("ContatoModel", back_populates="usuario")
    emprestimos = relationship("EmprestimoModel", back_populates="usuario")