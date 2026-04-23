from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ExemplarBase(BaseModel):
    codigo_localizacao: Optional[str] = Field(None, max_length=50)
    estado: str = Field(..., max_length=50)
    id_livro: int


class ExemplarCreate(ExemplarBase):
    pass


class ExemplarUpdate(BaseModel):
    codigo_localizacao: Optional[str] = Field(None, max_length=50)
    estado: Optional[str] = Field(None, max_length=50)


class ExemplarResponse(ExemplarBase):
    id_exemplar: int

    model_config = ConfigDict(from_attributes=True)