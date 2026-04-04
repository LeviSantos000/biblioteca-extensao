from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AutorBase(BaseModel):
    nome: str = Field(..., max_length=150)


class AutorCreate(AutorBase):
    pass


class AutorUpdate(BaseModel):
    nome: Optional[str] = Field(None, max_length=150)


class AutorResponse(AutorBase):
    id_autor: int

    model_config = ConfigDict(from_attributes=True)
