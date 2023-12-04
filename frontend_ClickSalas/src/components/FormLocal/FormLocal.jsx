import { useState } from "react";

export function FormLocal() {
  const [nomeLocal, setNomeLocal] = useState("");
  const [capacidadeLocal, setCapacidadeLocal] = useState("");
  const [mensagem, setMensagem] = useState("");

  const enviarDadosParaApi = async () => {
    const dadosLocal = {
      nome: nomeLocal,
      capacidade: parseInt(capacidadeLocal, 10),
    };

    console.log("Dados a serem enviados para a API:", dadosLocal);

    try {
      const response = await fetch("http://localhost:8000/enviar_local", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dadosLocal),
      });

      if (!response.ok) {
        throw new Error("Erro ao enviar dados para a API.");
      }

      setMensagem("Dados do local enviados com sucesso!");
    } catch (error) {
      console.error("Erro ao enviar dados do local:", error.message);
      setMensagem("Erro ao enviar dados do local. Tente novamente mais tarde.");
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    enviarDadosParaApi();
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="nomeLocal">Nome do Local:</label>
        <input
          type="text"
          id="nomeLocal"
          name="nomeLocal"
          value={nomeLocal}
          onChange={(e) => setNomeLocal(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="capacidadeLocal">Capacidade:</label>
        <input
          type="number"
          id="capacidadeLocal"
          name="capacidadeLocal"
          value={capacidadeLocal}
          onChange={(e) => setCapacidadeLocal(e.target.value)}
          required
          max={50}
        />
      </div>
      <button type="submit">Enviar</button>
      {mensagem && <p>{mensagem}</p>}
    </form>
  );
}
