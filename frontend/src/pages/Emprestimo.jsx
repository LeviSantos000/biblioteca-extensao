import React, { useState } from 'react';

export default function App() {
  const [emprestimos, setEmprestimos] = useState([
    {
      id: 1,
      nomePessoa: 'NomePessoa',
      nomeLivro: 'NomeLivro',
      dataRecebeu: '',
      dataDevolucao: '',
    },
  ]);

  const [novoEmprestimo, setNovoEmprestimo] = useState({
    nomePessoa: '',
    dataRecebeu: '',
    nomeLivro: '',
    dataDevolucao: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNovoEmprestimo((prev) => ({ ...prev, [name]: value }));
  };

  const handleAddEmprestimo = (e) => {
    e.preventDefault();
    if (!novoEmprestimo.nomePessoa || !novoEmprestimo.nomeLivro) return;

    setEmprestimos((prev) => [
      ...prev,
      {
        id: Date.now(),
        nomePessoa: novoEmprestimo.nomePessoa,
        nomeLivro: novoEmprestimo.nomeLivro,
        dataRecebeu: novoEmprestimo.dataRecebeu,
        dataDevolucao: novoEmprestimo.dataDevolucao,
      },
    ]);

    setNovoEmprestimo({ nomePessoa: '', dataRecebeu: '', nomeLivro: '', dataDevolucao: '' });
  };

  const emptySlotsCount = Math.max(0, 4 - emprestimos.length);

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
            Emprestimos
          </h1>
        </div>
      </div>

      <div className="max-w-5xl mx-auto px-4 flex flex-col md:flex-row justify-center items-start gap-10 md:gap-16">
        
        <form
          onSubmit={handleAddEmprestimo}
          className="bg-[#ebebeb] p-6 rounded-2xl w-full md:w-[350px] flex flex-col gap-4 shadow-[0_2px_10px_rgba(0,0,0,0.08)]"
        >
          <div className="flex gap-3">
            <input
              type="text"
              name="nomePessoa"
              value={novoEmprestimo.nomePessoa}
              onChange={handleInputChange}
              placeholder="NomePessoa"
              className="flex-[3] w-full bg-white px-3 py-2.5 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-xs sm:text-sm font-bold outline-none focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
            <input
              type="text"
              name="dataRecebeu"
              value={novoEmprestimo.dataRecebeu}
              onChange={handleInputChange}
              placeholder="DataRecebeu"
              className="flex-[2] w-full bg-white px-2 py-2.5 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-[11px] sm:text-xs font-bold outline-none text-center focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
          </div>
          
          <div className="flex gap-3">
            <input
              type="text"
              name="nomeLivro"
              value={novoEmprestimo.nomeLivro}
              onChange={handleInputChange}
              placeholder="NomeLivro"
              className="flex-[3] w-full bg-white px-3 py-2.5 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-xs sm:text-sm font-bold outline-none focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
            <input
              type="text"
              name="dataDevolucao"
              value={novoEmprestimo.dataDevolucao}
              onChange={handleInputChange}
              placeholder="DataDevolução"
              className="flex-[2] w-full bg-white px-2 py-2.5 rounded-full text-[#fc9d54] placeholder-[#fc9d54] text-[11px] sm:text-xs font-bold outline-none text-center focus:ring-2 focus:ring-orange-300 transition-all shadow-sm"
            />
          </div>

          <button
            type="submit"
            className="mt-4 mb-2 bg-white text-[#fc9d54] font-bold text-sm px-8 py-2.5 rounded-full shadow-[0_2px_8px_rgba(0,0,0,0.1)] self-center hover:bg-gray-50 active:scale-95 transition-all"
          >
            Adicionar
          </button>
        </form>

        <div className="bg-[#f2f2f2] p-8 rounded-2xl w-full md:w-[450px] flex flex-col gap-5 shadow-[0_2px_10px_rgba(0,0,0,0.08)] min-h-[450px]">
          
          {emprestimos.map((emprestimo) => (
            <div key={emprestimo.id} className="bg-[#d9d9d9] rounded-xl p-4 flex justify-between items-center h-[88px] shadow-sm">
              <div className="flex flex-col gap-1.5 text-black font-bold text-sm tracking-tight">
                <span className="truncate max-w-[200px]">{emprestimo.nomePessoa}</span>
                <span className="truncate max-w-[200px]">{emprestimo.nomeLivro}</span>
              </div>
              <div className="bg-white rounded-full w-[45px] h-[45px] flex items-center justify-center flex-shrink-0 shadow-sm">
              </div>
            </div>
          ))}

          {Array.from({ length: emptySlotsCount }).map((_, index) => (
            <div 
              key={`empty-${index}`} 
              className="bg-[#d9d9d9] rounded-xl p-4 h-[88px] shadow-sm opacity-80"
            ></div>
          ))}

        </div>
      </div>
    </div>
  );
}