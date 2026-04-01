from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from .autor import AutorResponse
from .categoria import CategoriaResponse


class LivroBase(BaseModel):
    titulo: str = Field(..., max_length=200)
    ano: Optional[int] = None
    issn: Optional[str] = Field(None, max_length=20)
    quantidade_exemplares: int = Field(default=0)
    id_autor: Optional[int] = None


class LivroCreate(LivroBase):
    id_categorias: List[int] = []


class LivroUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=200)
    ano: Optional[int] = None
    issn: Optional[str] = Field(None, max_length=20)
    quantidade_exemplares: Optional[int] = None
    id_autor: Optional[int] = None


class LivroResponse(LivroBase):
    id: int
    autor: Optional[AutorResponse] = None
    categorias: List[CategoriaResponse] = []

    model_config = ConfigDict(from_attributes=True)
