from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class RelatorioEmprestimoItem(BaseModel):
    id_emprestimo: int
    titulo_livro: str
    nome_usuario: str
    data_emprestimo: date
    data_prevista: date
    data_devolucao: Optional[date] = None
    status_atraso: bool = False


class RelatorioGeralResponse(BaseModel):
    data_geracao: date
    total_registros: int
    itens: List[RelatorioEmprestimoItem]
