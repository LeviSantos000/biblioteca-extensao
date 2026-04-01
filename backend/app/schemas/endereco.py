from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class EnderecoBase(BaseModel):
    rua: Optional[str] = Field(None, max_length=150)
    numero: Optional[str] = Field(None, max_length=20)
    complemento: Optional[str] = Field(None, max_length=100)
    cep: Optional[str] = Field(None, max_length=20)
    cidade: Optional[str] = Field(None, max_length=100)
    estado: Optional[str] = Field(None, max_length=50)
    id_bairro: Optional[int] = None


class EnderecoCreate(EnderecoBase):
    pass


class EnderecoUpdate(BaseModel):
    rua: Optional[str] = Field(None, max_length=150)
    numero: Optional[str] = Field(None, max_length=20)
    complemento: Optional[str] = Field(None, max_length=100)
    cep: Optional[str] = Field(None, max_length=20)
    cidade: Optional[str] = Field(None, max_length=100)
    estado: Optional[str] = Field(None, max_length=50)
    id_bairro: Optional[int] = None


class EnderecoResponse(EnderecoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
