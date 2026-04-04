const Login = () => {
    return (
    <>
        <div
        className="flex justify-center items-center w-screen h-screen bg-cover bg-center bg-no-repeat"
        style={{ backgroundImage: 'url(src/assets/library-background.png)' }}
        >
            <div className="w-md h-150 flex flex-col justify-between items-center bg-white rounded-[2.5rem] shadow-2xl">

                <h2 className="text-orange-400 text-4xl font-bold mt-10">
                    Login
                </h2>

                <div className="flex flex-col justify-center items-center ">

                        <input type="text" placeholder="Username" className="w-80 h-15 bg-gray-300 pl-5 rounded-md mb-5" />
                        <input type="text" placeholder="Password" className="w-80 h-15 bg-gray-300 pl-5 rounded-md"/>

                        <div className="w-full flex flex-row justify-between mt-2 text-blue-900 underline">
                            <div><a href="#">Esqueceu a senha?</a></div>
                            <div><a href="#">Cadastrar</a></div>
                        </div>

                </div>
               
                <button type="submit" className="flex justify-center items-center w-3xs h-15 bg-gray-400 text-3xl rounded-[1rem] mb-30 cursor-pointer">
                    Entrar
                </button>
               
            </div>
        </div>
    </>
    );
}
 
export default Login;