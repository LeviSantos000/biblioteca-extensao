from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CategoriaBase(BaseModel):
    categoria: str = Field(..., max_length=100)


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    categoria: Optional[str] = Field(None, max_length=100)


class CategoriaResponse(CategoriaBase):
    id_categoria: int

    model_config = ConfigDict(from_attributes=True)
