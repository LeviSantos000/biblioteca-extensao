from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class EmprestimoBase(BaseModel):
    data_emprestimo: date
    data_prevista: date
    data_devolucao: Optional[date] = None
    id_usuario: int
    id_exemplar: int


class EmprestimoCreate(EmprestimoBase):
    pass


class EmprestimoUpdate(BaseModel):
    data_prevista: Optional[date] = None
    data_devolucao: Optional[date] = None


class EmprestimoResponse(EmprestimoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
