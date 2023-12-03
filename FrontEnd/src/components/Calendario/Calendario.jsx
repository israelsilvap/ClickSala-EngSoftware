import styles from "./Calendario.module.css";

import iconCalendar from "../../assets/calendar 1.svg";

import { Link } from "react-router-dom";

export function Calendario() {
  return (
    <Link to="/">
      <div className={styles.buttonCalendar}>
        <img
          src={iconCalendar}
          alt="calendario"
          className={styles.iconCalendar}
        />
        <p>06/dez</p>
      </div>
    </Link>
  );
}
