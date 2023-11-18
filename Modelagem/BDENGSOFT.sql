CREATE DATABASE IF NOT EXISTS mydatabase;  
USE mydatabase;  

DROP TABLE IF EXISTS Sala;
DROP TABLE IF EXISTS Agenda;
DROP TABLE IF EXISTS Horarios;
DROP TABLE IF EXISTS Turma;
DROP TABLE IF EXISTS Dias_Aula_Docente;
DROP TABLE IF EXISTS Horarios_Aulas_Docente;
DROP TABLE IF EXISTS Disciplina;
DROP TABLE IF EXISTS Docente;
DROP FUNCTION IF EXISTS GetTurmaSuffix;


CREATE TABLE Docente (
    ID_Docente INT,
    Nome_Docente VARCHAR(255),
    PRIMARY KEY (ID_Docente)
);

CREATE TABLE Dias_Aula_Docente (
    ID_Dias_Aula INT,
    ID_Docente INT,
    Dias_Aula SET('segunda', 'terca', 'quarta', 'quinta', 'sexta'),
    PRIMARY KEY (ID_Dias_Aula),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Docente)
);
-- mexi nos horarios, mudei o padrao APENAS
CREATE TABLE Horarios_Aulas_Docente (
    ID_Horarios_Aulas INT,
    ID_Docente INT,
    Horarios_Aula SET('08h00_10h00', '10h00_12h00', '13h30_15h30', '15h30_17h30'),
    PRIMARY KEY (ID_Horarios_Aulas),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Docente)
);

CREATE TABLE Disciplina (
    ID_Disciplina INT,
    Nome_Disciplina VARCHAR(255),
    Tipo ENUM('obrigatoria', 'optativa'),
    Periodo INT,
    PRIMARY KEY (ID_Disciplina)
);

CREATE TABLE Turma (
    ID_Turma INT,
    Nome_Turma VARCHAR(255),
    ID_Disciplina INT,
    ID_Docente INT,    
    Num_Alunos INT,
    Dias_Aula SET('segunda', 'terca', 'quarta', 'quinta', 'sexta'),
    Horario_Aulas SET('08h00_10h00', '10h00_12h00', '13h30_15h30', '15h30_17h30'),
    PRIMARY KEY (ID_Turma),
    UNIQUE (Nome_Turma),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID_Disciplina),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Docente)
);

CREATE TABLE Horarios (
    ID_Horario INT AUTO_INCREMENT,
    08h00_10h00 VARCHAR(255),
    10h00_12h00 VARCHAR(255),
    13h30_15h30 VARCHAR(255),
    15h30_17h30 VARCHAR(255),
    PRIMARY KEY (ID_Horario),
    FOREIGN KEY (08h00_10h00) REFERENCES Turma(Nome_Turma),
    FOREIGN KEY (10h00_12h00) REFERENCES Turma(Nome_Turma),
    FOREIGN KEY (13h30_15h30) REFERENCES Turma(Nome_Turma),
    FOREIGN KEY (15h30_17h30) REFERENCES Turma(Nome_Turma)
);

CREATE TABLE Agenda (
    ID_Agenda INT AUTO_INCREMENT,
    Segunda INT,
    Terca INT,
    Quarta INT,
    Quinta INT,
    Sexta INT,
    PRIMARY KEY (ID_Agenda),
    FOREIGN KEY (Segunda)
        REFERENCES Horarios (ID_Horario),
    FOREIGN KEY (Terca)
        REFERENCES Horarios (ID_Horario),
    FOREIGN KEY (Quarta)
        REFERENCES Horarios (ID_Horario),
    FOREIGN KEY (Quinta)
        REFERENCES Horarios (ID_Horario),
    FOREIGN KEY (Sexta)
        REFERENCES Horarios (ID_Horario)
);

CREATE TABLE Sala (
    ID_Sala INT AUTO_INCREMENT,
    ID_Agenda INT,
    Nome VARCHAR(255),
    Capacidade INT,
    PRIMARY KEY (ID_Sala),
    FOREIGN KEY (ID_Agenda) REFERENCES Agenda(ID_Agenda)
);

-- FUNÇÕES DE GATILHO

DROP PROCEDURE IF EXISTS CreateSala;

DELIMITER //
CREATE PROCEDURE CreateSala(IN Nome VARCHAR(255), IN Capacidade INT)
BEGIN
    DECLARE ID_Agenda INT;
    DECLARE ID_Horario_Segunda INT;
    DECLARE ID_Horario_Terca INT;
    DECLARE ID_Horario_Quarta INT;
    DECLARE ID_Horario_Quinta INT;
    DECLARE ID_Horario_Sexta INT;

    -- Cria um novo registro na tabela Horarios para cada dia da semana
    INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES (NULL, NULL, NULL, NULL);
    SET ID_Horario_Segunda = LAST_INSERT_ID();
    INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES (NULL, NULL, NULL, NULL);
    SET ID_Horario_Terca = LAST_INSERT_ID();
    INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES (NULL, NULL, NULL, NULL);
    SET ID_Horario_Quarta = LAST_INSERT_ID();
    INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES (NULL, NULL, NULL, NULL);
    SET ID_Horario_Quinta = LAST_INSERT_ID();
    INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES (NULL, NULL, NULL, NULL);
    SET ID_Horario_Sexta = LAST_INSERT_ID();

    -- Cria um novo registro na tabela Agenda
    INSERT INTO Agenda (Segunda, Terca, Quarta, Quinta, Sexta)
    VALUES (ID_Horario_Segunda, ID_Horario_Terca, ID_Horario_Quarta, ID_Horario_Quinta, ID_Horario_Sexta);
    SET ID_Agenda = LAST_INSERT_ID();

    -- Cria um novo registro na tabela Sala
    INSERT INTO Sala (ID_Agenda, Nome, Capacidade)
    VALUES (ID_Agenda, Nome, Capacidade);
END//
DELIMITER ;

-- TRIGGER PARA TURMAS COM MESMA DISCIPLINA

DELIMITER //
CREATE FUNCTION GetTurmaSuffix(turma_count INT) RETURNS CHAR(4) DETERMINISTIC
BEGIN
    CASE turma_count
        WHEN 0 THEN RETURN '';
        WHEN 1 THEN RETURN ' - A';
        WHEN 2 THEN RETURN ' - B';
        WHEN 3 THEN RETURN ' - C';
        -- Adicione mais casos conforme necessário
    END CASE;
END;//
DELIMITER ;

DELIMITER //
CREATE TRIGGER set_turma_name BEFORE INSERT ON Turma
FOR EACH ROW
BEGIN
    DECLARE disciplina_nome VARCHAR(255);
    DECLARE turma_count INT;
    DECLARE turma_suffix CHAR(4);

    SELECT Nome_Disciplina INTO disciplina_nome FROM Disciplina WHERE ID_Disciplina = NEW.ID_Disciplina;
    SELECT COUNT(*) INTO turma_count FROM Turma WHERE ID_Disciplina = NEW.ID_Disciplina;

    SET turma_suffix = GetTurmaSuffix(turma_count);
    SET NEW.Nome_Turma = CONCAT(disciplina_nome, turma_suffix);
END;//
DELIMITER ;

-- ESTA TRIGGER IMPEDE A CRIAÇÃO DE TURMAS DUPLICADAS COM A MESMA DISCIPLINA, PROFESSOR, DIAS E HORÁRIOS.

DELIMITER //
CREATE TRIGGER check_turma BEFORE INSERT ON Turma
FOR EACH ROW
BEGIN
   IF EXISTS (SELECT 1 FROM Turma WHERE ID_Disciplina = NEW.ID_Disciplina AND ID_Docente = NEW.ID_Docente AND Dias_Aula = NEW.Dias_Aula AND Horario_Aulas = NEW.Horario_Aulas) THEN 
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Não é possível inserir turma duplicada.';
   END IF;
END;//
DELIMITER ;


