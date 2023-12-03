import mysql.connector

class BancoDeDados:
    def __init__(self) -> None:
        self.conexao = mysql.connector.connect(
            # host='db4free.net',
            # user='dnilson',
            # password= 'mat495986',
            # database= 'bdmat495986'

            host='localhost',
            user='root',
            password= '5991',
            database= 'mydatabase'
        )

    def inserirLocal(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.cursor = self.conexao.cursor()
        comando = f"CALL CreateSala('{nome}', {self.capacidade})"        
        try:
            self.cursor.execute(comando)
            self.conexao.commit()
            self.cursor.close()
            return True
        
        except Exception as e:
            self.cursor.close()
            return False        

    def inserirDocente(self, Nome_Docente, dias, horarios):
        self.Nome_Docente = Nome_Docente
        self.dias = dias
        self.horarios = horarios
        self.ID_Docente = 0
        self.cursor = self.conexao.cursor()
        comando = f"INSERT INTO Docente (Nome_Docente) VALUES ('{self.Nome_Docente}');"      
        try:
            self.cursor.execute(comando)
            self.conexao.commit()
            comando = f"SELECT ID_Docente FROM Docente WHERE Nome_Docente = '{self.Nome_Docente}'"
            self.cursor.execute((comando))
            self.ID_Docente = self.cursor.fetchall()[0][0]
            for i in range(len(dias)):                
                comando = f"INSERT INTO Dias_Aula_Docente (ID_Docente, Dias_Aula, Horarios_Aula) VALUES ({self.ID_Docente}, '{self.dias[i]}', '{self.horarios[i]}');"               
                self.cursor.execute(comando)
                self.conexao.commit()
            self.cursor.close()
            return True
        except Exception as e:
            self.cursor.close()
            return False
        
    def inserirDisciplina(self, Nome_Disciplina, Tipo, Periodo):
        self.Nome_Disciplina = Nome_Disciplina
        self.Tipo = Tipo
        self.Periodo = Periodo
        self.cursor = self.conexao.cursor()
        comando = f"INSERT INTO Disciplina (Nome_Disciplina, Tipo, Periodo) VALUES ('{self.Nome_Disciplina}', '{self.Tipo}', {self.Periodo});"      
        try:
            self.cursor.execute(comando)
            self.conexao.commit()
            self.cursor.close()
            return True
        except Exception as e:
            self.cursor.close()
            return False        

    def inserirTurma(self, Nome_Disciplina, Nome_Docente, Num_Alunos, Dias_Aula, Horario_Aulas):
        self.Nome_Disciplina = Nome_Disciplina
        self.Nome_Docente = Nome_Docente
        self.Num_Alunos = Num_Alunos
        self.Dias_Aula = Dias_Aula
        self.Horario_Aulas = Horario_Aulas
        self.ID_Disciplina = self.get_ID_Disciplina(self.Nome_Disciplina)
        self.ID_Docente = self.get_ID_Docente(self.Nome_Docente)
        comando = f"INSERT INTO Turma (ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horario_Aulas) VALUES ({self.ID_Disciplina}, {self.ID_Docente}, {self.Num_Alunos}, '{self.Dias_Aula}', '{self.Horario_Aulas}')"
        self.cursor = self.conexao.cursor()
        try:
            self.cursor.execute(comando)
            self.conexao.commit()
            self.cursor.close()
            return True
        except Exception as e:
            self.cursor.close()
            return False

    def get_ID_Disciplina(self, Nome_Disciplina):
        self.Nome_Disciplina = Nome_Disciplina
        self.cursor = self.conexao.cursor()
        comando = f"SELECT ID_Disciplina FROM Disciplina WHERE Nome_Disciplina = '{self.Nome_Disciplina}'"
        try:
            self.cursor.execute(comando)
            self.ID_Disciplina = self.cursor.fetchall()[0][0]
            self.cursor.close()
            return self.ID_Disciplina
        except Exception as e:
            self.cursor.close()
            return False

    
    def get_ID_Docente(self, Nome_Docente):
        self.Nome_Docente = Nome_Docente
        self.cursor = self.conexao.cursor()
        comando = f"SELECT ID_Docente FROM Docente WHERE Nome_Docente = '{self.Nome_Docente}'"
        try:
            self.cursor.execute(comando)
            self.ID_Docente = self.cursor.fetchall()[0][0]
            self.cursor.close()
            return self.ID_Docente
        except Exception as e:
            self.cursor.close()
            return False


