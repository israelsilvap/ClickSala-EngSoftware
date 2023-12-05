import "./../global.css";
import styles from "./../App.module.css";

import { Sidebar } from "./../components/Sidebar/Sidebar";
import { Card } from "./../components/Card/Card";
import { CardAtividades } from "./../components/CardAtividades/CardAtividades";

import { Link } from "react-router-dom";

import iconMeet from "./../assets/image 4.svg";
import iconClass from "./../assets/image 2.svg";
import iconSala from "./../assets/localsala.svg";
import iconBd from "./../assets/image 5.svg";
import iconLogout from "./../assets/icon-logout.svg";

export function Home() {
  return (
    <div className={styles.containerGlobal}>
      <div className={styles.wrapper}>
        <Sidebar />
      </div>

      <main>
        <div className={styles.containerTop}>
          <div className={styles.areacoord}>
            <h1>Área do Coordenador</h1>
          </div>
          <div className={styles.divLogout}>
            <Link to="/">
              <img src={iconLogout} alt="Logout" />
              Logout
            </Link>
          </div>
        </div>
        <div className={styles.container1}>
          <Card
            title="Alocação de Locais"
            icon={iconSala}
            description="Crie, gerencie ou exclua locais com facilidade, monitorando todas as atividades"
          />
          <Card
            title="Turmas"
            icon={iconClass}
            description="Crie, gerencie ou exclua turmas do seu banco de dados"
          />
          <Card
            title="Cronogramas"
            icon={iconMeet}
            description="Confira os cronogramas que foram gerados este semestre"
          />
        </div>
        <div className={styles.container2}>
          <CardAtividades />
          <Card
            link="/bdpage"
            title="Banco de dados"
            icon={iconBd}
            description="Gerencie informações sobre locais e pessoas de forma eficiente e organizada com um banco de dados Simplifique o acesso e a manipulação de dados"
          />
        </div>
      </main>
    </div>
  );
}
