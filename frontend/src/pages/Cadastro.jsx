import React from 'react';
import { User, Mail, Lock } from 'lucide-react';

export default function App() {
  return (
    <div 
      className="min-h-screen flex items-center justify-center bg-cover bg-center bg-no-repeat"
      style={{ backgroundImage: "assets/library-background.png" }}
    >
      <div className="bg-[#FFFFFF] rounded-[2.5rem] p-10 shadow-2xl w-full max-w-[380px] flex flex-col items-center">
        
        <h2 className="text-[#FF8A24] text-2xl font-bold mb-10 mt-2">
          Cadastro
        </h2>

        <div className="w-full space-y-5 px-2">
          <div className="relative flex items-center">
            <User className="absolute left-4 text-gray-600 w-5 h-5 stroke-[2.5]" />
            <input 
              type="text" 
              placeholder="Username" 
              className="w-full bg-[#D9D9D9] text-gray-800 placeholder-gray-500 rounded-xl py-3 pl-12 pr-4 focus:outline-none focus:ring-2 focus:ring-[#FF8A24]/50 transition-all font-medium"
            />
          </div>

          <div className="relative flex items-center">
            <Mail className="absolute left-4 text-gray-600 w-5 h-5 stroke-[2.5]" />
            <input 
              type="email" 
              placeholder="Email" 
              className="w-full bg-[#D9D9D9] text-gray-800 placeholder-gray-500 rounded-xl py-3 pl-12 pr-4 focus:outline-none focus:ring-2 focus:ring-[#FF8A24]/50 transition-all font-medium"
            />
          </div>

          <div className="relative flex items-center">
            <Lock className="absolute left-4 text-gray-600 w-5 h-5 stroke-[2.5]" />
            <input 
              type="password" 
              placeholder="Password" 
              className="w-full bg-[#D9D9D9] text-gray-800 placeholder-gray-500 rounded-xl py-3 pl-12 pr-4 focus:outline-none focus:ring-2 focus:ring-[#FF8A24]/50 transition-all font-medium"
            />
          </div>
        </div>

        <button className="mt-12 mb-4 bg-[#D9D9D9] hover:bg-[#CFCFCF] text-gray-800 font-semibold py-3 px-10 rounded-xl transition-colors duration-200">
          Cadastrar
        </button>

      </div>
    </div>
  );
}
