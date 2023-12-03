import styles from "./CardAtiv.module.css";

import { Link } from "react-router-dom";

export function CardAtividades() {
  return (
    <section>
      <Link to="/">
        <h3>Atividades Recentes</h3>
        <div className={styles.container}>
          <div className={styles.ativ1}>
            <p1>Aula</p1>
            <p2>Física 3</p2>
            <p3>Sala 11</p3>
          </div>
          <div className={styles.ativ2}>
            <p1>Aula</p1>
            <p2>Cálculo 2</p2>
            <p3>Sala 9</p3>
          </div>
          <div className={styles.ativ3}>
            <p1>Laboratório</p1>
            <p2>Programação</p2>
            <p3>Sala 10</p3>
          </div>
        </div>
      </Link>
    </section>
  );
}
