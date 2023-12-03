import { useState } from "react";
import styles from "./Modal.module.css";

import { FormDocente } from "./../FormDocente/FormDocente";

export function Modal() {
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
      <button onClick={toggleModal} className={styles.btnModal}>
        Adicionar Docente
      </button>

      {modal && (
        <div className={styles.modal}>
          <div onClick={toggleModal} className={styles.overlay}></div>
          <div className={styles.modalContent}>
            <FormDocente />
            <button className={styles.closeModal} onClick={toggleModal}>
              Fechar
            </button>
          </div>
        </div>
      )}
    </>
  );
}
