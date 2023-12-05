import "./../global.css";
import styles from "./../App.module.css";

import { Link } from "react-router-dom";

import iconVoltar from "./../assets/Voltar.svg";
import iconCamp from "./../assets/camp.jpg";

export function Campus() {
  return (
    <main className={styles.mainTeam}>
      <h1>Conheça nosso Campus</h1>
      <p>UFC - Universidade Federal do Ceará - Campus Sobral</p>
      <div className={styles.containerCamp}>
        <img src={iconCamp} alt="icon" className={styles.iconCamp} />
        <div className={styles.divCamp}>
          <h3>Campus Mucambinho</h3>
          <p>
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book. It has survived not
            only five centuries, but also the leap into electronic typesetting,
            remaining essentially unchanged. It was popularised in the 1960s
            with the release of Letraset sheets containing Lorem Ipsum passages,
            and more recently with desktop publishing software like Aldus
            PageMaker including versions of Lorem Ipsum.
          </p>
          <p>
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book. It has survived not
            only five centuries, but also the leap into electronic typesetting,
            remaining essentially unchanged. It was popularised in the 1960s
            with the release of Letraset sheets containing Lorem Ipsum passages,
            and more recently with desktop publishing software like Aldus
            PageMaker including versions of Lorem Ipsum.
          </p>
        </div>
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
