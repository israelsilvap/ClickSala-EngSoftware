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
        

    def inserirDocente(self, Nome_Docente):
        self.Nome_Docente = Nome_Docente
        self.cursor = self.conexao.cursor()
        comando = f"INSERT INTO Docente (Nome_Docente) VALUES ('{self.Nome_Docente}');"        
        try:
            self.cursor.execute(comando)
            self.conexao.commit()
            self.cursor.close()
            return True
        
        except Exception as e:
            self.cursor.close()
            return False
        
    def recuperarIdDocente(self, Nome_Docente):
        self.Nome_Docente = Nome_Docente
        self.cursor = self.conexao.cursor()
        comando = f"SELECT ID_Docente FROM Docente WHERE Nome_Docente = '{self.Nome_Docente}';"
        try:
            self.cursor.execute(comando)
            id_docente = self.cursor.fetchone()[0]
            self.cursor.close()
            return id_docente
        except Exception as e:
            self.cursor.close()
            return None

    def inserirHorarioDocente(self, ID_Docente, dias_aula, horarios_aula):
        self.ID_Docente = ID_Docente
        self.dias_aula = dias_aula
        self.horarios_aula = horarios_aula
        self.cursor = self.conexao.cursor()
        
        comando_dias = f"INSERT INTO Dias_Aula_Docente (ID_Docente, Dias_Aula) VALUES ({self.ID_Docente}, '{self.dias_aula}');"
        comando_horarios = f"INSERT INTO Horarios_Aulas_Docente (ID_Docente, Horarios_Aula) VALUES ({self.ID_Docente}, '{self.horarios_aula}');"
        
        try:
            self.cursor.execute(comando_dias)
            self.cursor.execute(comando_horarios)
            self.conexao.commit()
            self.cursor.close()
            return True
        except Exception as e:
            self.cursor.close()
            return False
