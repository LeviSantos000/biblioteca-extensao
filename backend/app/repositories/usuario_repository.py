from sqlalchemy.orm import Session
from app.models.usuario import UsuarioModel
from app.repositories.base_repository import BaseRepository

class UsuarioRepository(BaseRepository[UsuarioModel]):
    def __init__(self, db: Session):
        super().__init__(UsuarioModel, db)

    def get_all(self) -> list[UsuarioModel]:
        return self.db.query(self.model).all()

    def get_by_id(self, usuario_id: int) -> UsuarioModel | None:
        return self.db.query(self.model).filter(self.model.id == usuario_id).first()

    def get_by_cpf(self, cpf: str) -> UsuarioModel | None:
        return self.db.query(self.model).filter(self.model.cpf == cpf).first()

    def get_ativos(self) -> list[UsuarioModel]:
        return self.db.query(self.model).filter(self.model.ativo).all()