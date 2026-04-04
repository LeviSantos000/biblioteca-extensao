from fastapi import APIRouter

from app.api.livros import router as livros_router
from app.api.pessoas import router as pessoas_router
from app.api.emprestimos import router as emprestimos_router
from app.api.relatorios import router as relatorios_router

api_router = APIRouter()

api_router.include_router(livros_router, prefix="/livros", tags=["Livros"])
api_router.include_router(pessoas_router, prefix="/pessoas", tags=["Pessoas"])
api_router.include_router(emprestimos_router, prefix="/emprestimos", tags=["Emprestimos"])
api_router.include_router(relatorios_router, prefix="/relatorios", tags=["Relatorios"])