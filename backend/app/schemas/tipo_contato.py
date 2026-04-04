from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TipoContatoBase(BaseModel):
    tipo: str = Field(..., max_length=100)


class TipoContatoCreate(TipoContatoBase):
    pass


class TipoContatoUpdate(BaseModel):
    tipo: Optional[str] = Field(None, max_length=100)


class TipoContatoResponse(TipoContatoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
