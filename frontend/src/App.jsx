import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import Cadastro from "./pages/Cadastro";
import HomePage from "./pages/HomePage";
import Livros from "./pages/Livros";
import Emprestimos from "./pages/Emprestimos";
import EsqueceuSenha from "./pages/EsqueceuSenha";

const App = () => {
  return (
  <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />}/>
        <Route path="/cadastro" element={<Cadastro />}/>
        <Route path="/esqueceusenha" element={<EsqueceuSenha/>}/>
        <Route path="/home" element={<HomePage />} />
        <Route path="/livros" element={<Livros />} />
        <Route path="/emprestimos" element={<Emprestimos />} />
      </Routes>
    </BrowserRouter>
  </>
  );
}
 
export default App;