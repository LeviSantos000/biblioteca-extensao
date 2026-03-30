from sqlalchemy import Column, ForeignKey, Integer, Table
from app.core.database import Base

livro_categoria = Table(
    "livro_categoria",
    Base.metadata,
    Column("id_livro", Integer, ForeignKey("livro.id"), primary_key=True),
    Column("id_categoria", Integer, ForeignKey("categoria.id_categoria"), primary_key=True),
)