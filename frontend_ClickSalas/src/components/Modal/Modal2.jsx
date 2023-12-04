import { useState } from "react";
import styles from "./Modal.module.css";

import { FormDisciplina } from "../FormDisciplina/FormDisciplina";

export function Modal2() {
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
        Adicionar Disciplina
      </button>

      {modal && (
        <div className={styles.modal}>
          <div onClick={toggleModal} className={styles.overlay}></div>
          <div className={styles.modalContent}>
            <FormDisciplina />
            <button className={styles.closeModal} onClick={toggleModal}>
              Fechar
            </button>
          </div>
        </div>
      )}
    </>
  );
}
