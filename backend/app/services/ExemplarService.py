from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.exemplar import ExemplarModel
from app.schemas.exemplar import ExemplarCreate, ExemplarUpdate


class ExemplarService:
    def __init__(self, db: Session):
        self.db = db

    def listar(self) -> list[ExemplarModel]:
        return self.db.query(ExemplarModel).all()

    def buscar_por_id(self, exemplar_id: int) -> ExemplarModel:
        exemplar = self.db.query(ExemplarModel).filter(ExemplarModel.id_exemplar == exemplar_id).first()
        if not exemplar:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exemplar não encontrado")
        return exemplar

    def listar_por_livro(self, livro_id: int) -> list[ExemplarModel]:
        return self.db.query(ExemplarModel).filter(ExemplarModel.id_livro == livro_id).all()

    def criar(self, data: ExemplarCreate) -> ExemplarModel:
        exemplar = ExemplarModel(**data.model_dump())
        self.db.add(exemplar)
        self.db.commit()
        self.db.refresh(exemplar)
        return exemplar

    def atualizar(self, exemplar_id: int, data: ExemplarUpdate) -> ExemplarModel:
        exemplar = self.buscar_por_id(exemplar_id)
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(exemplar, field, value)
        self.db.commit()
        self.db.refresh(exemplar)
        return exemplar

    def deletar(self, exemplar_id: int) -> None:
        exemplar = self.buscar_por_id(exemplar_id)
        self.db.delete(exemplar)
        self.db.commit()