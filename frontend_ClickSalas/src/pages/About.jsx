import "./../global.css";
import styles from "./../App.module.css";

import { CardTeam } from "./../components/CardTeam/CardTeam";
import icon from "./../assets/alexandre.jpeg";
import icon2 from "./../assets/anderson.png";
import icon3 from "./../assets/Ozeas.png";
import icon4 from "./../assets/silvan.png";
import icon5 from "./../assets/israel.png";
import icon6 from "./../assets/dnilson.png";

import { Link } from "react-router-dom";

import iconVoltar from "./../assets/Voltar.svg";

export function About() {
  return (
    <main className={styles.mainTeam}>
      <h1>Conheça nosso time</h1>
      <p>UFC - Universidade Federal do Ceará</p>
      <div className={styles.containerTeam1}>
        <CardTeam
          cargo="Desenvolvedor Front-End"
          icon={icon}
          title="Alexandre Gomes"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
        <CardTeam
          cargo="Desenvolvedor Back-End"
          icon={icon2}
          title="Anderson Ivanildo"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
        <CardTeam
          cargo="Testador de Software"
          icon={icon3}
          title="Ozeas do Carmo"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
      </div>
      <div className={styles.containerTeam2}>
        <CardTeam
          cargo="Desenvolvedor Back-End"
          icon={icon6}
          title="Dnilson Sousa"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
        <CardTeam
          cargo="Desenvolvedor Back-End"
          icon={icon5}
          title="Israel da Silva"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
        <CardTeam
          cargo="Testador de Software"
          icon={icon4}
          title="Silvan Felipe"
          description="It is a long established fact that a reader will be distracted a page when looking at its layout. "
        />
      </div>
      <div className={styles.divVoltar}>
        <Link to="/">
          <div className={styles.btnVoltar2}>
            <img src={iconVoltar} alt="Icon" className={styles.iconVoltar2} />
            <p>Voltar</p>
          </div>
        </Link>
      </div>
    </main>
  );
}
