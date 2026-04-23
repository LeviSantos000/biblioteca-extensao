from datetime import date

from app.models.emprestimo import EmprestimoModel
from app.repositories.base_repository import BaseRepository
from sqlalchemy.orm import Session


class EmprestimoRepository(BaseRepository[EmprestimoModel]):
    def __init__(self, db: Session):
        super().__init__(EmprestimoModel, db)

    def get_all(self) -> list[EmprestimoModel]:
        return self.db.query(self.model).all()
    
    def get_by_id(self, emprestimo_id: int) -> EmprestimoModel | None:
        return self.db.query(self.model).filter(self.model.id == emprestimo_id).first()

    def get_atrasados(self) -> list[EmprestimoModel]:
        return (
            self.db.query(self.model)
            .filter(
                self.model.data_devolucao is None,
                self.model.data_prevista < date.today(),
            )
            .all()
        )

    def registrar_devolucao(self, emprestimo_id: int):
        emprestimo = self.get_by_id(emprestimo_id)
        if emprestimo:
            emprestimo.data_devolucao = date.today()
            self.db.commit()
            return emprestimo
        return None
