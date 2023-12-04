import "./../global.css";
import styles from "./../App.module.css";

import { Link } from "react-router-dom";

import { Modal } from "../components/Modal/Modal";
import { Modal2 } from "../components/Modal/Modal2";
import { Modal3 } from "../components/Modal/Modal3";
import { Modal4 } from "../components/Modal/Modal4";

import iconVoltar from "./../assets/Voltar.svg";
import iconDocente from "./../assets/docente.svg";
import iconDisc from "./../assets/image 1.svg";
import iconTurma from "./../assets/iconTurma.svg";
import iconSala from "./../assets/iconSala.svg";

export function BdPage() {
  return (
    <div className={styles.containerGlobal}>
      <main>
        <div className={styles.containerTop}>
          <div className={styles.containerBd}>
            <h1>Banco de Dados</h1>
            <Link to="/">
              <div className={styles.btnVoltar}>
                <img
                  src={iconVoltar}
                  alt="Icon"
                  className={styles.iconVoltar}
                />
                <p>Voltar</p>
              </div>
            </Link>
          </div>
        </div>
        <div className={styles.containerBd2}>
          <div className={styles.card}>
            <img src={iconDocente} alt="Icon" className={styles.cardIcon} />
            <h3>Docentes</h3>
            <Modal />
            <Link to="/">
              <button className={styles.btnAlocacao}>Listar Docentes</button>
            </Link>
          </div>
          <div className={styles.card}>
            <img src={iconDisc} alt="Icon" className={styles.cardIcon} />
            <h3>Disciplinas</h3>

            <Modal2 />
            <Link to="/">
              <button className={styles.btnAlocacao}>Listar Disciplinas</button>
            </Link>
          </div>
          <div className={styles.card}>
            <img src={iconSala} alt="Icon" className={styles.cardIcon} />
            <h3>Locais</h3>

            <Modal3 />
            <Link to="/">
              <button className={styles.btnAlocacao}>Listar Locais</button>
            </Link>
          </div>
          <div className={styles.card}>
            <img src={iconTurma} alt="Icon" className={styles.cardIcon} />
            <h3>Turmas</h3>

            <Modal4 />
            <Link to="/">
              <button className={styles.btnAlocacao}>Listar Turmas</button>
            </Link>
          </div>
        </div>
        <div className={styles.contentAlocacao}>
          <Link to="/">
            <button className={styles.btnAlocacao}>Fazer Alocação</button>
          </Link>
        </div>
      </main>
    </div>
  );
}
