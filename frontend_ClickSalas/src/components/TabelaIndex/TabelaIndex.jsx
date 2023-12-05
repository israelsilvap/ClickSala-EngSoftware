import "./TabelaIndex.module.css";

export function TabelaIndex() {
  const horarios = ["08h-10h", "10h-12h", "13h30-15h30", "15h30-17h30"];
  const salas1 = Array.from({ length: 5 }, (_, i) => `Sala ${i + 1}`);
  const salas2 = Array.from({ length: 5 }, (_, i) => `Sala ${i + 6}`);
  const disciplinas = [
    "Cálculo I",
    "Física II",
    "Eng de Software",
    "Programação",
    "Palestra",
    "Banco de Dados",
    "Inteligência Comp",
    "---",
    "Circuitos",
  ];

  return (
    <div className="divTabela">
      <h3>Atividades de Hoje</h3>

      {/* Div para as Salas 01 até 05 */}
      <div style={{ float: "left", marginRight: "20px" }}>
        <table border="1">
          <thead>
            <tr>
              <th>Horário</th>
              {salas1.map((sala) => (
                <th key={sala}>{sala}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {horarios.map((horario) => (
              <tr key={horario}>
                <td>{horario}</td>
                {salas1.map((sala) => (
                  <td key={sala}>
                    {
                      disciplinas[
                        Math.floor(Math.random() * disciplinas.length)
                      ]
                    }
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Div para as Salas 06 até 10 */}
      <div style={{ float: "left" }}>
        <table border="1">
          <thead>
            <tr>
              <th>Horário</th>
              {salas2.map((sala) => (
                <th key={sala}>{sala}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {horarios.map((horario) => (
              <tr key={horario}>
                <td>{horario}</td>
                {salas2.map((sala) => (
                  <td key={sala}>
                    {
                      disciplinas[
                        Math.floor(Math.random() * disciplinas.length)
                      ]
                    }
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div style={{ clear: "both" }}></div>
    </div>
  );
}
