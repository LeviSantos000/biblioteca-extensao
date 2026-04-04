from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base

class EmprestimoModel(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_emprestimo = Column(Date, nullable=False)
    data_prevista = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    id_exemplar = Column(Integer, ForeignKey("exemplar.id_exemplar"), nullable=False)

    usuario = relationship("UsuarioModel", back_populates="emprestimos")
    exemplar = relationship("ExemplarModel", back_populates="emprestimos")