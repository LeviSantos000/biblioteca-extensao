from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.LivroService import LivroService
from app.schemas.livro import LivroCreate, LivroUpdate, LivroResponse

router = APIRouter()


@router.get("/", response_model=list[LivroResponse])
def listar_livros(
    titulo: str | None = Query(default=None, description="Filtrar por título"),
    db: Session = Depends(get_db),
):
    service = LivroService(db)
    if titulo:
        return service.buscar_por_titulo(titulo)
    return service.listar()


@router.get("/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    return LivroService(db).buscar_por_id(livro_id)


@router.post("/", response_model=LivroResponse, status_code=201)
def criar_livro(data: LivroCreate, db: Session = Depends(get_db)):
    return LivroService(db).criar(data)


@router.put("/{livro_id}", response_model=LivroResponse)
def atualizar_livro(livro_id: int, data: LivroUpdate, db: Session = Depends(get_db)):
    return LivroService(db).atualizar(livro_id, data)


@router.delete("/{livro_id}", status_code=204)
def deletar_livro(livro_id: int, db: Session = Depends(get_db)):
    LivroService(db).deletar(livro_id)