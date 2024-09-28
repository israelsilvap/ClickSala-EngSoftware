import styles from "./CardTeam.module.css";

import icon1 from "./../../assets/github.svg";
import icon2 from "./../../assets/linkedin.png";
import icon3 from "./../../assets/instagram.png";

export function CardTeam(props) {
  return (
    <div className={styles.cardTeam}>
      <div className={styles.imgTeam}>
        <img src={props.icon} alt="Icon" className={styles.cardIcon2} />
      </div>
      <div className={styles.descriptionTeam}>
        <h4>{props.cargo}</h4>
        <h3>{props.title}</h3>
        <p>{props.description}</p>
        <div className={styles.divIcons}>
          <img src={icon1} alt="Iconredes" className={styles.iconRedes} />
          <img src={icon2} alt="Iconredes" className={styles.iconRedes} />
          <img src={icon3} alt="Iconredes" className={styles.iconRedes} />
        </div>
      </div>
    </div>
  );
}
