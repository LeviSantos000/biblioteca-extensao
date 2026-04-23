from sqlalchemy.orm import Session
from app.models.livro import LivroModel
from app.repositories.base_repository import BaseRepository

class LivroRepository(BaseRepository[LivroModel]):
    def __init__(self, db: Session):
        super().__init__(LivroModel, db)

    def get_all(self):
        return self.db.query(self.model).all()
    
    def get_by_id(self, livro_id: int) -> LivroModel | None:
        return self.db.query(self.model).filter(self.model.id == livro_id).first()

    def get_by_titulo(self, titulo: str) -> list[LivroModel]:
        return self.db.query(self.model).filter(self.model.titulo.ilike(f"%{titulo}%")).all()

    def verificar_estoque(self, livro_id: int) -> int:
        livro = self.get_by_id(livro_id)
        return livro.quantidade_exemplares if livro else 0