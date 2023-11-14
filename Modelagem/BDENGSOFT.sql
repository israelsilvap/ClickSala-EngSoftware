CREATE DATABASE IF NOT EXISTS mydatabase;  -- Cria o banco de dados se ele não existir
USE mydatabase;  -- Seleciona o banco de dados

DROP TABLE IF EXISTS Sala;
DROP TABLE IF EXISTS Agenda;
DROP TABLE IF EXISTS Horarios;
DROP TABLE IF EXISTS Turma;
DROP TABLE IF EXISTS Disciplina;
DROP TABLE IF EXISTS Docente;


CREATE TABLE Docente (
    ID_Docente INT,
    Nome VARCHAR(255),
    Horario_Aulas SET('08:00-10:00', '10:00-12:00', '13:30-15:30', '15:30-17:30'),
    Dias_Aula SET('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'),
    PRIMARY KEY (ID_Docente)
);

CREATE TABLE Disciplina (
    ID_Disciplina INT,
    Nome VARCHAR(255),
    Tipo ENUM('obrigatoria', 'optativa'),
    Periodo INT,
    PRIMARY KEY (ID_Disciplina)
);

CREATE TABLE Turma (
    ID_Turma INT,
    ID_Disciplina INT,
    ID_Docente INT,
    Num_Alunos INT,
    Dias_Aula SET('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'),
    Horario_Aulas SET('08:00-10:00', '10:00-12:00', '13:30-15:30', '15:30-17:30'),
    PRIMARY KEY (ID_Turma),
    FOREIGN KEY (ID_Disciplina) REFERENCES Disciplina(ID_Disciplina),
    FOREIGN KEY (ID_Docente) REFERENCES Docente(ID_Docente)
);

CREATE TABLE Horarios (
    ID_Horario INT,
    Primeiro INT,
    Segundo  INT,
    Terceiro INT,
    Quarto   INT,
    PRIMARY KEY (ID_Horario),
    FOREIGN KEY (Primeiro) REFERENCES Turma(ID_Turma),
    FOREIGN KEY (Segundo) REFERENCES Turma(ID_Turma),
    FOREIGN KEY (Terceiro) REFERENCES Turma(ID_Turma),
    FOREIGN KEY (Quarto) REFERENCES Turma(ID_Turma)
);


CREATE TABLE Agenda (
    ID_Agenda INT,
    Segunda  INT,
    Terca    INT,
    Quarta   INT,
    Quinta   INT,
    Sexta    INT,
    PRIMARY KEY (ID_Agenda),
    FOREIGN KEY (Segunda) REFERENCES Horarios(ID_Horario),
    FOREIGN KEY (Terca) REFERENCES Horarios(ID_Horario),
    FOREIGN KEY (Quarta) REFERENCES Horarios(ID_Horario),
    FOREIGN KEY (Quinta) REFERENCES Horarios(ID_Horario),
    FOREIGN KEY (Sexta) REFERENCES Horarios(ID_Horario)
);


CREATE TABLE Sala (
    ID_Sala INT,
    ID_Agenda INT,
    Nome VARCHAR(255),
    Capacidade INT,
    PRIMARY KEY (ID_Sala),
    FOREIGN KEY (ID_Agenda) REFERENCES Agenda(ID_Agenda)
);
