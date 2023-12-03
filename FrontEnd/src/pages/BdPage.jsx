import "./../global.css";
import styles from "./../App.module.css";

import { Link } from "react-router-dom";

import { Modal } from "../components/Modal/Modal";

import iconVoltar from "./../assets/Voltar.svg";
import iconDocente from "./../assets/docente.svg";
import iconLocal from "./../assets/local.svg";

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
          </div>
          <div className={styles.card}>
            <img src={iconLocal} alt="Icon" className={styles.cardIcon} />
            <h3>Locais</h3>

            <Modal />
          </div>
        </div>
      </main>
    </div>
  );
}
