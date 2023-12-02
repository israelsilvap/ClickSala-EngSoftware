-- Inserindo professores
INSERT INTO Docente (ID_Docente, Nome_Docente) VALUES 
(1, 'Prof. João'), 
(2, 'Prof. Maria'),
(3, 'Prof. Ana'),
(4, 'Prof. Carlos'),
(5, 'Prof. Beatriz');

-- Povoando a tabela Dias_Aula_Docente
INSERT INTO Dias_Aula_Docente (ID_Docente, Dias_Aula, Horarios_Aula) VALUES 
(1, 'segunda', '08h00_10h00,10h00_12h00'),
(1, 'quarta', '13h30_15h30,15h30_17h30'),
(1, 'quinta', '08h00_10h00,10h00_12h00'),
(2, 'segunda', '13h30_15h30,15h30_17h30'),
(2, 'terca', '08h00_10h00,10h00_12h00'),
(2, 'sexta', '08h00_10h00,10h00_12h00');



-- Povoando a tabela Disciplina
INSERT INTO Disciplina (ID_Disciplina, Nome_Disciplina, Tipo, Periodo) VALUES 
(1, 'Matemática', 'obrigatoria', 1), 
(2, 'História', 'optativa', 2),
(3, 'Física', 'obrigatoria', 1),
(4, 'Química', 'optativa', 2),
(5, 'Biologia', 'obrigatoria', 1),
(6, 'Geografia', 'optativa', 2),
(7, 'Português', 'obrigatoria', 1),
(8, 'Inglês', 'optativa', 2),
(9, 'Educação Física', 'obrigatoria', 1),
(10, 'Artes', 'optativa', 2);

-- Inserindo turmas
INSERT INTO Turma (ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horario_Aulas) VALUES 
(1, 1, 30, 'segunda,quarta', '08h00_10h00'),
(2, 1, 30, 'sexta', '10h00_12h00'),
(3, 2, 30, 'terca', '13h30_15h30'),
(4, 2, 30, 'quinta', '15h30_17h30'),
(5, 3, 30, 'segunda', '08h00_10h00'),
(6, 3, 30, 'quarta', '10h00_12h00'),
(7, 4, 30, 'terca', '13h30_15h30'),
(8, 4, 30, 'quinta', '15h30_17h30'),
(9, 5, 30, 'segunda', '08h00_10h00'),
(10, 5, 30, 'sexta', '10h00_12h00');

-- Inserindo salas
CALL CreateSala('Sala 101', 30);
CALL CreateSala('Sala 102', 25);
CALL CreateSala('Sala 103', 35);
CALL CreateSala('Sala 104', 40);
CALL CreateSala('Sala 105', 45);

