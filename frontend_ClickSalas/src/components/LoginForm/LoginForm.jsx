// LoginForm.js
import { useState } from "react";

import "./LoginForm.module.css";

import { Link } from "react-router-dom";

export function LoginForm() {
  const [usuario, setUsuario] = useState("");
  const [senha, setSenha] = useState("");
  const [mensagem, setMensagem] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aqui você pode adicionar a lógica de autenticação ou envio dos dados para a API
    console.log("Usuário:", usuario);
    console.log("Senha:", senha);
    setMensagem(
      "Tentativa de login (lógica de autenticação não implementada)."
    );
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Login</h3>
      <div>
        <label htmlFor="usuario">Usuário:</label>
        <input
          type="text"
          id="usuario"
          name="usuario"
          value={usuario}
          onChange={(e) => setUsuario(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="senha">Senha:</label>
        <input
          type="password"
          id="senha"
          name="senha"
          value={senha}
          onChange={(e) => setSenha(e.target.value)}
          required
        />
      </div>
      <Link to="/home">
        <button type="submit">Entrar</button>
      </Link>
      {mensagem && <p>{mensagem}</p>}
    </form>
  );
}
