from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class AutorModel(Base):
    __tablename__ = "autor"

    id_autor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)

    livros = relationship("LivroModel", back_populates="autor")