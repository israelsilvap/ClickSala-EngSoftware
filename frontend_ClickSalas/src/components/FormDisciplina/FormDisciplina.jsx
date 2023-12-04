// FormDisciplina.js
import { useState } from "react";

export function FormDisciplina() {
  const [nomeDisciplina, setNomeDisciplina] = useState("");
  const [tipoDisciplina, setTipoDisciplina] = useState("Obrigatório");
  const [periodoDisciplina, setPeriodoDisciplina] = useState("");
  const [mensagem, setMensagem] = useState("");

  const enviarDadosParaApi = async () => {
    const dadosDisciplina = {
      nome: nomeDisciplina,
      tipo: tipoDisciplina,
      periodo:
        tipoDisciplina === "Obrigatório"
          ? parseInt(periodoDisciplina, 10)
          : null,
    };

    console.log("Dados a serem enviados para a API:", dadosDisciplina);

    try {
      const response = await fetch("http://localhost:8000/enviar_disciplina", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dadosDisciplina),
      });

      if (!response.ok) {
        throw new Error("Erro ao enviar dados para a API.");
      }

      setMensagem("Dados da disciplina enviados com sucesso!");
    } catch (error) {
      console.error("Erro ao enviar dados da disciplina:", error.message);
      setMensagem(
        "Erro ao enviar dados da disciplina. Tente novamente mais tarde."
      );
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    enviarDadosParaApi();
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="nomeDisciplina">Nome da Disciplina:</label>
        <input
          type="text"
          id="nomeDisciplina"
          name="nomeDisciplina"
          value={nomeDisciplina}
          onChange={(e) => setNomeDisciplina(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="tipoDisciplina">Tipo:</label>
        <select
          id="tipoDisciplina"
          name="tipoDisciplina"
          value={tipoDisciplina}
          onChange={(e) => setTipoDisciplina(e.target.value)}
          required
        >
          <option value="Obrigatório">Obrigatório</option>
          <option value="Optativa">Optativa</option>
        </select>
      </div>
      {tipoDisciplina === "Obrigatório" && (
        <div>
          <label htmlFor="periodoDisciplina">Período:</label>
          <input
            type="number"
            id="periodoDisciplina"
            name="periodoDisciplina"
            value={periodoDisciplina}
            onChange={(e) => setPeriodoDisciplina(e.target.value)}
            required={tipoDisciplina === "Obrigatório"}
            min={1}
            max={10}
          />
        </div>
      )}
      <button type="submit">Enviar</button>
      {mensagem && <p>{mensagem}</p>}
    </form>
  );
}
