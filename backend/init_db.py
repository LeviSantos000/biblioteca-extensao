from app.core.database import engine, Base

from app.models.associations import * 
from app.models.autor import AutorModel
from app.models.categoria import CategoriaModel
from app.models.contato import ContatoModel
from app.models.emprestimo import EmprestimoModel
from app.models.endereco import EnderecoModel
from app.models.exemplar import ExemplarModel
from app.models.livro import LivroModel
from app.models.tipo_contato import TipoContatoModel
from app.models.usuario import UsuarioModel

def init_db():
    print("Iniciando o script...")
    print("Conectando ao banco de dados no Supabase...")
    
   
    Base.metadata.create_all(bind=engine)
    
    print("Tabelas criadas com sucesso! Vá checar o Supabase.")


if __name__ == "__main__":
    init_db()
