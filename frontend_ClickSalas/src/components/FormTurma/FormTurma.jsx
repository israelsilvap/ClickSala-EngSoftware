import { useState } from "react";

export function FormTurma() {
  const [nomeDisciplina, setNomeDisciplina] = useState("");
  const [nomeDocente, setNomeDocente] = useState("");
  const [numeroAlunos, setNumeroAlunos] = useState("");
  const [diasSemana, setDiasSemana] = useState([]);
  const [horario, setHorario] = useState("");
  const [mensagem, setMensagem] = useState("");

  const enviarDadosParaApi = async () => {
    const dadosTurma = {
      nomeDisciplina,
      nomeDocente,
      numeroAlunos: parseInt(numeroAlunos, 10),
      diasSemana,
      horario,
    };

    console.log("Dados a serem enviados para a API:", dadosTurma);

    try {
      const response = await fetch("http://localhost:8000/enviar_turma", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dadosTurma),
      });

      if (!response.ok) {
        throw new Error("Erro ao enviar dados para a API.");
      }

      setMensagem("Dados da turma enviados com sucesso!");
    } catch (error) {
      console.error("Erro ao enviar dados da turma:", error.message);
      setMensagem("Erro ao enviar dados da turma. Tente novamente mais tarde.");
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
        <label htmlFor="nomeDocente">Nome do Docente:</label>
        <input
          type="text"
          id="nomeDocente"
          name="nomeDocente"
          value={nomeDocente}
          onChange={(e) => setNomeDocente(e.target.value)}
          required
        />
      </div>
      <div>
        <label htmlFor="numeroAlunos">Número de Alunos:</label>
        <input
          type="number"
          id="numeroAlunos"
          name="numeroAlunos"
          value={numeroAlunos}
          onChange={(e) => setNumeroAlunos(e.target.value)}
          required
        />
      </div>
      <div>
        <label>Dias da Semana:</label>
        <div>
          <label>
            <input
              type="checkbox"
              name="segunda"
              checked={diasSemana.includes("segunda")}
              onChange={() => setDiasSemana(["segunda"])}
            />
            Segunda
          </label>
          <label>
            <input
              type="checkbox"
              name="terca"
              checked={diasSemana.includes("terca")}
              onChange={() => setDiasSemana(["terca"])}
            />
            Terça
          </label>
          <label>
            <input
              type="checkbox"
              name="quarta"
              checked={diasSemana.includes("quarta")}
              onChange={() => setDiasSemana(["quarta"])}
            />
            Quarta
          </label>
          <label>
            <input
              type="checkbox"
              name="quinta"
              checked={diasSemana.includes("quinta")}
              onChange={() => setDiasSemana(["quinta"])}
            />
            Quinta
          </label>
          <label>
            <input
              type="checkbox"
              name="sexta"
              checked={diasSemana.includes("sexta")}
              onChange={() => setDiasSemana(["sexta"])}
            />
            Sexta
          </label>
        </div>
      </div>
      <div>
        <label htmlFor="horario">Horário:</label>
        <input
          type="text"
          id="horario"
          name="horario"
          value={horario}
          onChange={(e) => setHorario(e.target.value)}
          required
        />
      </div>
      <button type="submit">Enviar</button>
      {mensagem && <p>{mensagem}</p>}
    </form>
  );
}
