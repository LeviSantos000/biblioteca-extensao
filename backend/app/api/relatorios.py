from datetime import date

from app.core.database import get_db
from app.models.emprestimo import EmprestimoModel
from app.models.exemplar import ExemplarModel
from app.models.livro import LivroModel
from app.models.usuario import UsuarioModel
from app.repositories.relatorio_repository import RelatorioRepository
from app.schemas.relatorio import RelatorioEmprestimoItem, RelatorioGeralResponse
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/emprestimos", response_model=RelatorioGeralResponse)
def relatorio_emprestimos(db: Session = Depends(get_db)):
    resultados = (
        db.query(
            EmprestimoModel,
            LivroModel.titulo,
            UsuarioModel.nome,
        )
        .join(ExemplarModel, EmprestimoModel.id_exemplar == ExemplarModel.id_exemplar)
        .join(LivroModel, ExemplarModel.id_livro == LivroModel.id)
        .join(UsuarioModel, EmprestimoModel.id_usuario == UsuarioModel.id)
        .all()
    )

    hoje = date.today()
    itens = [
        RelatorioEmprestimoItem(
            id_emprestimo=emp.id,
            titulo_livro=titulo,
            nome_usuario=nome,
            data_emprestimo=emp.data_emprestimo,
            data_prevista=emp.data_prevista,
            data_devolucao=emp.data_devolucao,
            status_atraso=(emp.data_devolucao is None and emp.data_prevista < hoje),
        )
        for emp, titulo, nome in resultados
    ]

    return RelatorioGeralResponse(
        data_geracao=hoje,
        total_registros=len(itens),
        itens=itens,
    )


@router.get("/livros-mais-emprestados")
def livros_mais_emprestados(db: Session = Depends(get_db)):
    repo = RelatorioRepository(db)
    resultado = repo.livros_mais_emprestados()
    return [
        {"titulo": titulo, "total_emprestimos": total} for titulo, total in resultado
    ]
