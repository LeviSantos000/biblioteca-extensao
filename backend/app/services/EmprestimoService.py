from app.models.emprestimo import EmprestimoModel
from app.models.exemplar import ExemplarModel
from app.repositories.emprestimo_repository import EmprestimoRepository
from app.schemas.emprestimo import EmprestimoCreate, EmprestimoUpdate
from fastapi import HTTPException, status
from sqlalchemy.orm import Session


class EmprestimoService:
    def __init__(self, db: Session):
        self.repo = EmprestimoRepository(db)
        self.db = db

    def listar(self) -> list[EmprestimoModel]:
        return self.repo.get_all()

    def buscar_por_id(self, emprestimo_id: int) -> EmprestimoModel:
        emprestimo = self.repo.get_by_id(emprestimo_id)
        if not emprestimo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empréstimo não encontrado",
            )
        return emprestimo
    
    def buscar_por_cpf(self, cpf: str) -> list[EmprestimoModel]:
        return self.repo.get_by_cpf(cpf)

    def listar_atrasados(self) -> list[EmprestimoModel]:
        return self.repo.get_atrasados()

    def criar(self, data: EmprestimoCreate) -> EmprestimoModel:
        exemplar = (
            self.db.query(ExemplarModel)
            .filter(ExemplarModel.id_exemplar == data.id_exemplar)
            .first()
        )
        if not exemplar:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Exemplar não encontrado"
            )

        emprestimo_ativo = (
            self.db.query(EmprestimoModel)
            .filter(
                EmprestimoModel.id_exemplar == data.id_exemplar,
                EmprestimoModel.data_devolucao is None,
            )
            .first()
        )
        if emprestimo_ativo:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Exemplar já está emprestado",
            )

        emprestimo = EmprestimoModel(**data.model_dump())
        return self.repo.create(emprestimo)

    def atualizar(self, emprestimo_id: int, data: EmprestimoUpdate) -> EmprestimoModel:
        emprestimo = self.buscar_por_id(emprestimo_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(emprestimo, field, value)
        return self.repo.update(emprestimo)

    def registrar_devolucao(self, emprestimo_id: int) -> EmprestimoModel:
        emprestimo = self.repo.registrar_devolucao(emprestimo_id)
        if not emprestimo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empréstimo não encontrado",
            )
        return emprestimo

    def deletar(self, emprestimo_id: int) -> None:
        self.buscar_por_id(emprestimo_id)
        self.repo.delete(emprestimo_id)
