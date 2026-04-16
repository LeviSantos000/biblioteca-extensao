import { Mail, ArrowLeft } from 'lucide-react';
import backgroundImage from '../assets/library-background.png';

export default function EsqueceuSenha() {
  return (
    <div 
      className="min-h-screen flex items-center justify-center bg-cover bg-center bg-no-repeat"
      style={{ backgroundImage: `url(${backgroundImage})` }}
    >
      <div className="bg-[#FFFFFF] rounded-[2.5rem] p-10 shadow-2xl w-full max-w-95 flex flex-col items-center">
        
        <h2 className="text-[#FF8A24] text-2xl font-bold mb-4 mt-2">
          Recuperar Senha
        </h2>
        
        <p className="text-gray-500 text-center text-sm mb-10 px-4">
          Digite seu e-mail abaixo para receber as instruções de recuperação.
        </p>

        <div className="w-full space-y-5 px-2">
          <div className="relative flex items-center">
            <Mail className="absolute left-4 text-gray-600 w-5 h-5 stroke-[2.5]" />
            <input 
              type="email" 
              placeholder="Email cadastrado" 
              className="w-full bg-[#D9D9D9] text-gray-800 placeholder-gray-500 rounded-xl py-3 pl-12 pr-4 focus:outline-none focus:ring-2 focus:ring-[#FF8A24]/50 transition-all font-medium"
            />
          </div>
        </div>

        <button className="mt-10 mb-6 bg-[#D9D9D9] hover:bg-[#CFCFCF] text-gray-800 font-semibold py-3 px-10 rounded-xl transition-colors duration-200 w-full max-w-[200px]">
          Enviar
        </button>

        <div className='relative flex items-center pt-2 text-sm text-gray-600 self-center'>
          <a href="/" className="flex items-center gap-2 hover:text-[#FF8A24] transition-colors">
            <ArrowLeft size={16} /> Voltar para o Login
          </a>
        </div>

      </div>
    </div>
  );
}