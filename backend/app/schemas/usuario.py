from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class UsuarioBase(BaseModel):
    nome: str = Field(..., max_length=100)
    tipo: Optional[str] = Field(None, max_length=50)
    data_nascimento: Optional[date] = None
    cpf: str = Field(..., max_length=14)
    sexo: Optional[str] = Field(None, max_length=1)
    status: bool = True
    id_endereco: Optional[int] = None


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = Field(None, max_length=100)
    tipo: Optional[str] = Field(None, max_length=50)
    data_nascimento: Optional[date] = None
    status: Optional[bool] = None
    id_endereco: Optional[int] = None


class UsuarioResponse(UsuarioBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
