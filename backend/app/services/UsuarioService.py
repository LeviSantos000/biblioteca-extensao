from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.usuario import UsuarioModel
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate


class UsuarioService:
    def __init__(self, db: Session):
        self.repo = UsuarioRepository(db)

    def listar(self) -> list[UsuarioModel]:
        return self.repo.get_all()

    def buscar_por_id(self, usuario_id: int) -> UsuarioModel:
        usuario = self.repo.get_by_id(usuario_id)
        if not usuario:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        return usuario

    def buscar_por_cpf(self, cpf: str) -> UsuarioModel:
        usuario = self.repo.get_by_cpf(cpf)
        if not usuario:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        return usuario

    def listar_ativos(self) -> list[UsuarioModel]:
        return self.repo.get_ativos()

    def criar(self, data: UsuarioCreate) -> UsuarioModel:
        existente = self.repo.get_by_cpf(data.cpf)
        if existente:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="CPF já cadastrado")
        usuario = UsuarioModel(**data.model_dump())
        return self.repo.create(usuario)

    def atualizar(self, usuario_id: int, data: UsuarioUpdate) -> UsuarioModel:
        usuario = self.buscar_por_id(usuario_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(usuario, field, value)
        return self.repo.update(usuario)

    def deletar(self, usuario_id: int) -> None:
        self.buscar_por_id(usuario_id)
        self.repo.delete(usuario_id)