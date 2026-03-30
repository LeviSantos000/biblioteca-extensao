from fastapi import APIRouter

# A variável que o Uvicorn está procurando!
router = APIRouter()

@router.get("/")
def listar_pessoas():
    return {"mensagem": "Rota de pessoas funcionando!"}