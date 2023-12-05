import styles from "./Sidebar.module.css";

import logoClick from "../../assets/Logo Click.svg";
import iconLogout from "../../assets/icon-logout.svg";
import logoHome from "../../assets/dashboards 1.svg";
import imgUfc from "../../assets/ufc.svg";
import logoCampus from "../../assets/campus.svg";
import logoTeam from "../../assets/group 1.svg";

import { Link } from "react-router-dom";

export function Sidebar() {
  return (
    <aside className={styles.sidebar}>
      <div className={styles.logo}>
        <img src={logoClick} alt="Logotipo" />
      </div>
      <div className={styles.home}>
        <Link to="/home">
          <img src={logoHome} alt="Logohome" />
          <p>Página Inicial</p>
        </Link>
      </div>
      <div className={styles.home}>
        <Link to="/about">
          <img src={logoTeam} alt="Logoteam" />
          <p>Quem somos</p>
        </Link>
      </div>
      <div className={styles.home}>
        <Link to="/campus">
          <img src={logoCampus} alt="Logocampus" />
          <p>Nosso Campus</p>
        </Link>
      </div>
      <div className={styles.ufc}>
        <img src={imgUfc} alt="imgUfc" />
      </div>
      <footer>
        <p>Todos os Direitos Reservados ©</p>
      </footer>
    </aside>
  );
}
