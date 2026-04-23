from app.models.categoria import CategoriaModel
from app.models.livro import LivroModel
from app.repositories.livro_repository import LivroRepository
from app.schemas.livro import LivroCreate, LivroUpdate
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


class LivroService:
    def __init__(self, db: Session):
        self.repo = LivroRepository(db)
        self.db = db

    def listar(self) -> list[LivroModel]:
        return self.repo.get_all()

    def buscar_por_id(self, livro_id: int) -> LivroModel:
        livro = self.repo.get_by_id(livro_id)
        if not livro:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado"
            )
        return livro

    def buscar_por_titulo(self, titulo: str) -> list[LivroModel]:
        return self.repo.get_by_titulo(titulo)

    def criar(self, data: LivroCreate) -> LivroModel:
        categorias = []
        if data.id_categorias:
            categorias = (
                self.db.query(CategoriaModel)
                .filter(CategoriaModel.id_categoria.in_(data.id_categorias))
                .all()
            )

        livro = LivroModel(
            titulo=data.titulo,
            ano=data.ano,
            issn=data.issn,
            quantidade_exemplares=data.quantidade_exemplares,
            id_autor=data.id_autor,
            categorias=categorias,
        )
        return self.repo.create(livro)

    def atualizar(self, livro_id: int, data: LivroUpdate) -> LivroModel:
        livro = self.buscar_por_id(livro_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(livro, field, value)
        return self.repo.update(livro)

    def deletar(self, livro_id: int) -> None:
        self.buscar_por_id(livro_id)
        self.repo.delete(livro_id)
