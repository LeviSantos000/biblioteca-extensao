from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.UsuarioService import UsuarioService
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter()


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(
    apenas_ativos: bool = Query(default=False, description="Retornar apenas usuários ativos"),
    db: Session = Depends(get_db),
):
    service = UsuarioService(db)
    if apenas_ativos:
        return service.listar_ativos()
    return service.listar()


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return UsuarioService(db).buscar_por_id(usuario_id)


@router.get("/cpf/{cpf}", response_model=UsuarioResponse)
def buscar_por_cpf(cpf: str, db: Session = Depends(get_db)):
    return UsuarioService(db).buscar_por_cpf(cpf)


@router.post("/", response_model=UsuarioResponse, status_code=201)
def criar_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService(db).criar(data)


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    return UsuarioService(db).atualizar(usuario_id, data)


@router.delete("/{usuario_id}", status_code=204)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    UsuarioService(db).deletar(usuario_id)