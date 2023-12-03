import styles from "./Card.module.css";

import { Link } from "react-router-dom";

export function Card(props) {
  return (
    <div className={styles.card}>
      <Link to={props.link}>
        <img src={props.icon} alt="Icon" className={styles.cardIcon} />
        <h3>{props.title}</h3>
        <p>{props.description}</p>
      </Link>
    </div>
  );
}
