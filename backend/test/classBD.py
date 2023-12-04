import mysql.connector
from classTurma import Turma
from classSala import Sala

class BancoDeDados:
    __instance = None

    @staticmethod 
    def getInstance():
        if BancoDeDados.__instance == None:
            BancoDeDados()
        return BancoDeDados.__instance

    def __init__(self):
        if BancoDeDados.__instance != None:
            raise Exception("Esta classe é um singleton!")
        else:
            BancoDeDados.__instance = self
            self.conexao = mysql.connector.connect(
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
        self.ID_Disciplina = self.getIDDisciplina(self.Nome_Disciplina)
        self.ID_Docente = self.getIDDocente(self.Nome_Docente)
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

    def getIDDisciplina(self, Nome_Disciplina):
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
    
    def getIDDocente(self, Nome_Docente):
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
        
    def getTurmaNames(self):
        self.cursor = self.conexao.cursor()
        # Obter nomes de todas as turmas
        command = 'SELECT Nome_Turma FROM Turma'
        self.cursor.execute(command)
        # Armazenar todos os nomes de turmas em uma lista
        turma_names = [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        return turma_names

    def getSalasNames(self):
        self.cursor = self.conexao.cursor()
        # Obter nomes de todas as turmas
        command = 'SELECT Nome FROM Sala'
        self.cursor.execute(command)
        # Armazenar todos os nomes de turmas em uma lista
        salas_names = [row[0] for row in self.cursor.fetchall()]
        self.cursor.close()
        return salas_names

    def createTurmaFromDB(self):
        turma_names = self.getTurmaNames()
        self.cursor = self.conexao.cursor()
        turmas = []
        for i in turma_names:
            # Obter informações da turma
            command = f"SELECT ID_Disciplina, Num_Alunos, Dias_Aula, Horario_Aulas FROM Turma WHERE Nome_Turma = '{i}'"
            self.cursor.execute(command)
            ID_Disciplina, Num_Alunos, Dias_Aula, Horario_Aulas = self.cursor.fetchone()
            # Obter informações da disciplina
            command = f'SELECT Nome_Disciplina, Tipo, Periodo FROM Disciplina WHERE ID_Disciplina = {ID_Disciplina}'
            self.cursor.execute(command)
            Nome, Tipo, Periodo  = self.cursor.fetchone()
            # Criar objeto de turma
            turma = Turma(Nome, Tipo, Periodo, Num_Alunos, Dias_Aula, Horario_Aulas)
            turmas.append(turma)
        self.cursor.close()
        return turmas

    # ACESSA O BANCO DE DADOS PARA OBTER AS INFORMAÇÕES
    def createSalaFromDB(self):
        salas_names = self.getSalasNames()
        self.cursor = self.conexao.cursor()
        salas = []
        for i in salas_names:
            # Obter informações da sala
            command = f"SELECT Nome, Capacidade, ID_Agenda FROM Sala WHERE Nome = '{i}'"
            self.cursor.execute(command)
            Nome, Capacidade, ID_Agenda = self.cursor.fetchone()
            # Obter informações da agenda
            command = f'SELECT Segunda, Terca, Quarta, Quinta, Sexta FROM Agenda WHERE ID_Agenda = {ID_Agenda}'
            self.cursor.execute(command)
            ID_Horario_Segunda, ID_Horario_Terca, ID_Horario_Quarta, ID_Horario_Quinta, ID_Horario_Sexta = self.cursor.fetchone()
            # Criar objeto de sala
            sala = Sala(Nome, Capacidade)
            # Para cada dia da semana, obter o horário correspondente e preencher a agenda da sala
            for dia, ID_Horario in zip(['segunda', 'terca', 'quarta', 'quinta', 'sexta'], [ID_Horario_Segunda, ID_Horario_Terca, ID_Horario_Quarta, ID_Horario_Quinta, ID_Horario_Sexta]):
                command = f'SELECT 08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30 FROM Horarios WHERE ID_Horario = {ID_Horario}'
                self.cursor.execute(command)
                horario = self.cursor.fetchone()
                sala.dias[dia].horarios = {
                    '08h00_10h00' : horario[0],
                    '10h00_12h00' : horario[1],
                    '13h30_15h30' : horario[2],
                    '15h30_17h30' : horario[3],
                }
            salas.append(sala)
        self.cursor.close()
        return salas


    def updateSalaInDB(self, sala):
        self.cursor = self.conexao.cursor()
        # Obter o ID da sala
        command = f"SELECT ID_Sala FROM Sala WHERE Nome = '{sala.Nome}'"
        self.cursor.execute(command)
        ID_Sala = self.cursor.fetchone()[0]
        # Para cada dia da semana, obtenha o ID do registro Horarios correspondente e atualize-o
        for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
            horario = sala.dias[dia].horarios
            dia = dia.capitalize()
            # Obter o ID do registro Horarios
            command = f"SELECT {dia} FROM Agenda WHERE ID_Agenda = (SELECT ID_Agenda FROM Sala WHERE ID_Sala = {ID_Sala})"
            command = command.replace("'None'", "NULL")
            self.cursor.execute(command)
            ID_Horario = self.cursor.fetchone()[0]
            # Atualizar o registro Horarios
            command = f"UPDATE Horarios SET 08h00_10h00 = '{horario['08h00_10h00']}', 10h00_12h00 = '{horario['10h00_12h00']}', 13h30_15h30 = '{horario['13h30_15h30']}', 15h30_17h30 = '{horario['15h30_17h30']}' WHERE ID_Horario = {ID_Horario}"
            command = command.replace("'None'", "NULL")
            self.cursor.execute(command)
        # Commit das alterações
        self.conexao.commit()

    # ALOCAÇÃO
    def alocarTurmas(self):
        # Criando uma lista de turmas
        turmas = self.createTurmaFromDB()
        # Criando uma lista de salas
        salas = self.createSalaFromDB()        
        # Ordenar as turmas por período (crescente), e em seguida por número de alunos (decrescente)
        turmas.sort(key=lambda x: (x.Periodo, -x.Num_Alunos))        
        # Iterar sobre as turmas
        for turma in turmas:
            # Iterar sobre as salas
            for sala in salas:
                # Verificar se a sala tem capacidade suficiente e está disponível nos dias e horários que a turma precisa
                if sala.Capacidade >= turma.Num_Alunos and sala.is_available(turma.Dias_Aula, turma.Horario_Aulas):
                    # Alocar a turma na sala
                    sala.allocate(turma)
                    print("OK!")
                    # Passar para a próxima turma
                    break
        for sala in salas:
            self.updateSalaInDB(sala)
    
    # RESETE ALOCAÇÃO
    def reseteHorarios(self):
        try:
            # Desativar temporariamente o modo de atualização seguro
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SET SQL_SAFE_UPDATES = 0;")
            # Atualizar a tabela Horarios
            command = """
            UPDATE Horarios
            SET
              `08h00_10h00` = NULL,
              `10h00_12h00` = NULL,
              `13h30_15h30` = NULL,
              `15h30_17h30` = NULL
            WHERE ID_Horario IS NOT NULL;
            """
            self.cursor.execute(command)
            # Reativar o modo de atualização seguro
            self.cursor.execute("SET SQL_SAFE_UPDATES = 1;")
            # Confirmar as alterações no banco de dados
            self.conexao.commit()
            print("Horarios resetados com sucesso!")
        except Exception as e:
            print(f"Erro ao resetar Horarios: {e}")
        finally:
            # Fechar o cursor
            self.cursor.close()

    def resetarSala(self, nome_sala):
        try:
            # Desativar temporariamente o modo de atualização seguro
            self.cursor = self.conexao.cursor()
            self.cursor.execute("SET SQL_SAFE_UPDATES = 0;")

            # Atualizar os horários na tabela Horarios para a sala especificada pelo Nome
            command = f"""
            UPDATE Horarios
            SET
            `08h00_10h00` = NULL,
            `10h00_12h00` = NULL,
            `13h30_15h30` = NULL,
            `15h30_17h30` = NULL
            WHERE ID_Horario IN (
            SELECT Segunda FROM Agenda WHERE ID_Agenda IN (SELECT ID_Agenda FROM Sala WHERE Nome = '{nome_sala}')
            UNION
            SELECT Terca FROM Agenda WHERE ID_Agenda IN (SELECT ID_Agenda FROM Sala WHERE Nome = '{nome_sala}')
            UNION
            SELECT Quarta FROM Agenda WHERE ID_Agenda IN (SELECT ID_Agenda FROM Sala WHERE Nome = '{nome_sala}')
            UNION
            SELECT Quinta FROM Agenda WHERE ID_Agenda IN (SELECT ID_Agenda FROM Sala WHERE Nome = '{nome_sala}')
            UNION
            SELECT Sexta FROM Agenda WHERE ID_Agenda IN (SELECT ID_Agenda FROM Sala WHERE Nome = '{nome_sala}')
            );
            """
            self.cursor.execute(command)

            # Reativar o modo de atualização seguro
            self.cursor.execute("SET SQL_SAFE_UPDATES = 1;")

            # Confirmar as alterações no banco de dados
            self.conexao.commit()
            print(f"Horários da Sala '{nome_sala}' resetados com sucesso!")
        except Exception as e:
            print(f"Erro ao resetar horários da Sala '{nome_sala}': {e}")
        finally:
            # Fechar o cursor
            self.cursor.close()
