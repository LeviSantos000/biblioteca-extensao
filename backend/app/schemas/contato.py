from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ContatoBase(BaseModel):
    contato: str = Field(..., max_length=150)
    status: bool = Field(default=True)
    id_tipo_contato: int
    id_usuario: int


class ContatoCreate(ContatoBase):
    pass


class ContatoUpdate(BaseModel):
    contato: Optional[str] = Field(None, max_length=150)
    status: Optional[bool] = None


class ContatoResponse(ContatoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
