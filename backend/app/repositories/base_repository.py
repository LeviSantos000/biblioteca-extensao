from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

# Define um tipo genérico
T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T], db: Session):
        self.model = model
        self.db = db

