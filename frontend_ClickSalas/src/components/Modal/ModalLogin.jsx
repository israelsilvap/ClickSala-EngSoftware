import { useState } from "react";
import styles from "./Modal.module.css";

import iconLogin from "./../../assets/login.png";
import { LoginForm } from "../LoginForm/LoginForm";

export function ModalLogin() {
  const [modal, setModal] = useState(false);

  const toggleModal = () => {
    setModal(!modal);
  };

  if (modal) {
    document.body.classList.add("activeModal");
  } else {
    document.body.classList.remove("activeModal");
  }

  return (
    <>
      <button onClick={toggleModal} className={styles.divLogout}>
        <img src={iconLogin} alt="Login" />
        Login
      </button>

      {modal && (
        <div className={styles.modal}>
          <div onClick={toggleModal} className={styles.overlay}></div>
          <div className={styles.modalContent}>
            <LoginForm />
            <button className={styles.closeModal} onClick={toggleModal}>
              Fechar
            </button>
          </div>
        </div>
      )}
    </>
  );
}
