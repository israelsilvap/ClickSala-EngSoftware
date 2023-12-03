import { useState } from "react";
import "./FormDocente.module.css";

export function FormDocente() {
  const [nome, setNome] = useState("");
  const [dias, setDias] = useState([]);
  const [horarios, setHorarios] = useState({
    segunda: [],
    terca: [],
    quarta: [],
    quinta: [],
    sexta: [],
  });
  const [mensagem, setMensagem] = useState("");

  const diasDaSemana = ["segunda", "terca", "quarta", "quinta", "sexta"];
  const horariosDisponiveis = [
    "8h-10h",
    "10h-12h",
    "13:30h-15:30h",
    "15:30h-17:30h",
  ];

  const handleInputChange = (e) => {
    const { name, value, type } = e.target;
    if (type === "checkbox") {
      setDias((prevDias) =>
        prevDias.includes(name)
          ? prevDias.filter((dia) => dia !== name)
          : [...prevDias, name]
      );
    } else if (name === "nome") {
      setNome(value);
    }
  };

  const handleHorarioChange = (dia, horario) => {
    setHorarios((prevHorarios) => {
      const horariosParaDia = prevHorarios[dia];
      if (horariosParaDia.includes(horario)) {
        return {
          ...prevHorarios,
          [dia]: horariosParaDia.filter((h) => h !== horario),
        };
      } else {
        return { ...prevHorarios, [dia]: [...horariosParaDia, horario] };
      }
    });
  };

  const enviarDadosParaBanco = async () => {
    const dadosDoFormulario = {
      nome,
      dias,
      horarios,
    };

    try {
      const response = await fetch("http://localhost:8000/adicionardocente", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(dadosDoFormulario),
      });

      if (!response.ok) {
        throw new Error("Erro ao enviar dados para o servidor.");
      }

      setMensagem("Dados enviados com sucesso!");
    } catch (error) {
      console.error("Erro ao enviar dados:", error.message);
      setMensagem("Erro ao enviar dados. Tente novamente mais tarde.");
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    enviarDadosParaBanco();
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="nome">Nome:</label>
        <input
          type="text"
          id="nome"
          name="nome"
          value={nome}
          onChange={handleInputChange}
        />
      </div>
      <div>
        <label>Dias da Semana:</label>
        {diasDaSemana.map((dia) => (
          <label key={dia}>
            <input
              type="checkbox"
              name={dia}
              checked={dias.includes(dia)}
              onChange={handleInputChange}
            />
            {dia.charAt(0).toUpperCase() + dia.slice(1)}
          </label>
        ))}
      </div>
      <div>
        <label>Horários Disponíveis:</label>
        {diasDaSemana.map((dia) => (
          <div key={dia}>
            <p>{dia.charAt(0).toUpperCase() + dia.slice(1)}:</p>
            {horariosDisponiveis.map((horario) => (
              <label key={horario}>
                <input
                  type="checkbox"
                  name={horario}
                  checked={horarios[dia].includes(horario)}
                  onChange={() => handleHorarioChange(dia, horario)}
                />
                {horario}
              </label>
            ))}
          </div>
        ))}
      </div>
      <button type="submit">Enviar</button>
      {mensagem && <p>{mensagem}</p>}
    </form>
  );
}
