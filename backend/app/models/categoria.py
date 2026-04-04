from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.associations import livro_categoria

class CategoriaModel(Base):
    __tablename__ = "categoria"

    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(100), nullable=False, unique=True)

    livros = relationship(
        "LivroModel",
        secondary=livro_categoria,
        back_populates="categorias"
    )