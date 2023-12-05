import "./../global.css";
import styles from "./../App.module.css";

import { Sidebar } from "../components/Sidebar/Sidebar";
import { TabelaIndex } from "../components/TabelaIndex/TabelaIndex";

import { Link } from "react-router-dom";

import { ModalLogin } from "../components/Modal/ModalLogin";

export function Index() {
  return (
    <div className={styles.containerGlobal}>
      <div className={styles.wrapper}>
        <Sidebar />
      </div>

      <main>
        <div className={styles.containerTop}>
          <div className={styles.areacoord}>
            <h1>Visão Geral</h1>
            <p>
              Verifique os horários diários referente a cada sala em nossa
              plataforma
            </p>
          </div>

          <ModalLogin />
        </div>
        <div className={styles.containerTable}>
          <TabelaIndex />
        </div>
      </main>
    </div>
  );
}
