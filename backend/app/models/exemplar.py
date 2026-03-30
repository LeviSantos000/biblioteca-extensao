from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class ExemplarModel(Base):
    __tablename__ = "exemplar"

    id_exemplar = Column(Integer, primary_key=True, autoincrement=True)
    codigo_localizacao = Column(String(50), nullable=True)
    estado = Column(String(50), nullable=False)
    id_livro = Column(Integer, ForeignKey("livro.id"), nullable=False)

    livro = relationship("LivroModel", back_populates="exemplares")
    emprestimos = relationship("EmprestimoModel", back_populates="exemplar")