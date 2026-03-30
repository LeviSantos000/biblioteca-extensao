from fastapi import APIRouter

# Aqui está a variável 'router' que o Uvicorn tanto procura!
router = APIRouter()

@router.get("/")
def listar_livros():
    return {"mensagem": "Rota de livros funcionando perfeitamente!"}