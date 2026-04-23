from app.core.database import get_db
from app.schemas.emprestimo import (
    EmprestimoCreate,
    EmprestimoResponse,
    EmprestimoUpdate,
)
from app.services.EmprestimoService import EmprestimoService
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=list[EmprestimoResponse])
def listar_emprestimos(
    atrasados: bool = Query(
        default=False, description="Retornar apenas empréstimos atrasados"
    ),
    db: Session = Depends(get_db),
):
    service = EmprestimoService(db)
    if atrasados:
        return service.listar_atrasados()
    return service.listar()


@router.get("/{emprestimo_id}", response_model=EmprestimoResponse)
def buscar_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    return EmprestimoService(db).buscar_por_id(emprestimo_id)


@router.post("/", response_model=EmprestimoResponse, status_code=201)
def criar_emprestimo(data: EmprestimoCreate, db: Session = Depends(get_db)):
    return EmprestimoService(db).criar(data)


@router.put("/{emprestimo_id}", response_model=EmprestimoResponse)
def atualizar_emprestimo(
    emprestimo_id: int, data: EmprestimoUpdate, db: Session = Depends(get_db)
):
    return EmprestimoService(db).atualizar(emprestimo_id, data)


@router.patch("/{emprestimo_id}/devolver", response_model=EmprestimoResponse)
def registrar_devolucao(emprestimo_id: int, db: Session = Depends(get_db)):
    return EmprestimoService(db).registrar_devolucao(emprestimo_id)


@router.delete("/{emprestimo_id}", status_code=204)
def deletar_emprestimo(emprestimo_id: int, db: Session = Depends(get_db)):
    EmprestimoService(db).deletar(emprestimo_id)
