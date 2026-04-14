import React, { useState } from 'react';

export default function App() {
  const [livros, setLivros] = useState([
    {
      id: 1,
      nome: 'NomeLivro',
      categoria: 'CategoriaLivro',
      quant: 'EstoqueQuantidade',
    },
  ]);

  const [novoLivro, setNovoLivro] = useState({
    nome: '',
    quant: '',
    categoria: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNovoLivro((prev) => ({ ...prev, [name]: value }));
  };

  const handleAddLivro = (e) => {
    e.preventDefault();
    if (!novoLivro.nome || !novoLivro.categoria || !novoLivro.quant) return;

    setLivros((prev) => [
      ...prev,
      {
        id: Date.now(),
        nome: novoLivro.nome,
        categoria: novoLivro.categoria,
        quant: novoLivro.quant,
      },
    ]);

    setNovoLivro({ nome: '', quant: '', categoria: '' });
  };

  const handleRemoveLivro = (idToRemove) => {
    setLivros((prev) => prev.filter((livro) => livro.id !== idToRemove));
  };

  const emptySlotsCount = Math.max(0, 3 - livros.length);

  return (
    <div className="min-h-screen bg-white overflow-hidden font-sans pb-12">
      <div className="w-full flex justify-center -mt-[120px] sm:-mt-[150px] mb-12">
        <div className="w-[800px] h-[300px] bg-[#fca867] border-[4px] border-[#2b9bf4] rounded-[50%] flex items-end justify-center pb-8 gap-4 shadow-sm">
          <div className="relative w-14 h-16 flex items-end">
            <div className="absolute right-0 bottom-0 w-10 h-16 bg-[#5c2ef4] rounded-sm shadow-sm"></div>
            <div className="absolute right-1 bottom-0 w-1 h-16 bg-[#4a1ed4] rounded-sm"></div>
            <div className="absolute left-0 bottom-0 w-11 h-14 bg-[#2b9bf4] rounded-sm border-r-4 border-[#1e82d4] shadow-md flex justify-center">
              <div className="w-4 h-1 bg-[#85c8f9] rounded-full mt-2 opacity-80"></div>
            </div>
          </div>
          <h1 className="text-white text-4xl font-extrabold tracking-wide mb-2">
            Livros
          </h1>
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-4 flex flex-col md:flex-row justify-center items-start gap-10 md:gap-16">
        
        <form
          onSubmit={handleAddLivro}
          className="bg-[#ebebeb] p-6 rounded-2xl w-full md:w-[350px] flex flex-col gap-4 shadow-[0_2px_10px_rgba(0,0,0,0.08)]"
        >
          <div className="flex gap-4">
            <input
              type="text"
              name="nome"
              value={novoLivro.nome}
              onChange={handleInputChange}
              placeholder="Nome"
              className="flex-1 bg-white px-4 py-2 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-sm font-bold outline-none focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
            <input
              type="text"
              name="quant"
              value={novoLivro.quant}
              onChange={handleInputChange}
              placeholder="Quant"
              className="w-[80px] bg-white px-4 py-2 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-sm font-bold outline-none text-center focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
          </div>
          
          <input
            type="text"
            name="categoria"
            value={novoLivro.categoria}
            onChange={handleInputChange}
            placeholder="Categoria"
            className="w-[70%] bg-white px-4 py-2 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-sm font-bold outline-none focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
          />

          <button
            type="submit"
            className="mt-6 mb-2 bg-white text-[#fc9d54] font-bold text-sm px-6 py-2.5 rounded-full shadow-[0_2px_8px_rgba(0,0,0,0.1)] self-center hover:bg-gray-50 active:scale-95 transition-all"
          >
            Adicionar livros
          </button>
        </form>

        <div className="bg-[#f2f2f2] p-8 rounded-2xl w-full md:w-[500px] flex flex-col gap-5 shadow-[0_2px_10px_rgba(0,0,0,0.08)] min-h-[450px]">
          
          {livros.map((livro) => (
            <div key={livro.id} className="flex items-center gap-4">
              <div className="bg-[#d9d9d9] rounded-xl p-4 flex-1 flex justify-between items-center h-24 shadow-sm">
                <div className="flex flex-col gap-1.5 text-black font-bold text-sm tracking-tight">
                  <span className="truncate max-w-[180px]">{livro.nome}</span>
                  <span className="truncate max-w-[180px]">{livro.categoria}</span>
                  <span className="truncate max-w-[180px]">{livro.quant}</span>
                </div>
                <div className="bg-white rounded-full w-[60px] h-[60px] flex items-center justify-center flex-shrink-0 shadow-sm">
                  <span className="text-[9px] font-extrabold text-center leading-[1.1] text-black">
                    Estoque<br />Atual
                  </span>
                </div>
              </div>
              
              <button
                onClick={() => handleRemoveLivro(livro.id)}
                className="w-[26px] h-[26px] bg-[#fc9d54] rounded-full text-white flex items-center justify-center text-xl font-bold shadow-sm hover:bg-[#f58d3d] active:scale-90 transition-all flex-shrink-0 pb-1"
                aria-label="Remover livro"
              >
                -
              </button>
            </div>
          ))}

          {Array.from({ length: emptySlotsCount }).map((_, index) => (
            <div key={`empty-${index}`} className="flex items-center gap-4">
              <div className="bg-[#d9d9d9] rounded-xl p-4 flex-1 h-24 shadow-sm opacity-80"></div>
              <div className="w-[26px] h-[26px] bg-[#fc9d54] rounded-full text-white flex items-center justify-center text-xl font-bold shadow-sm flex-shrink-0 opacity-80 pb-1">
                -
              </div>
            </div>
          ))}

        </div>
      </div>
    </div>
  );
}