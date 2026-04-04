from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.associations import livro_categoria

class LivroModel(Base):
    __tablename__ = "livro"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    ano = Column(Integer, nullable=True)
    issn = Column(String(20), nullable=True)
    quantidade_exemplares = Column(Integer, default=0, nullable=False)
    id_autor = Column(Integer, ForeignKey("autor.id_autor"), nullable=True)

    autor = relationship("AutorModel", back_populates="livros")
    categorias = relationship(
        "CategoriaModel",
        secondary=livro_categoria,
        back_populates="livros"
    )
    exemplares = relationship("ExemplarModel", back_populates="livro")