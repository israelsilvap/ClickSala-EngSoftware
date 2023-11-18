# Esse codigo cria uma instancia de TURMA apartir das 
# informações que estão no banco de dados.
# sera importante uma vez que as informações tem que vir do banco de dados
# para a memoria do computador para poder organizar


# LEMBRE-SE QUE SEMPRE QUE QUISER CRIAR UMA TURMA, 
# O BANCO DE DADOS DEVE POSSUIR DISCIPLINAS E DOCENTES 

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '5991',
    database= 'mydatabase'
)


# CLASSE TURMA
class Turma:
    def __init__(self, Nome, Tipo, Periodo, Num_Alunos, Dias_Aula, Horario_Aulas):
        self.Nome = Nome
        self.Tipo = Tipo
        self.Periodo = Periodo
        self.Num_Alunos = Num_Alunos
        self.Dias_Aula = Dias_Aula
        self.Horario_Aulas = Horario_Aulas

    def imprimir_nome(self):
        print(self.Nome)

    def imprimir_tipo(self):
        print(self.Tipo)

    def imprimir_periodo(self):
        print(self.Periodo)

    def imprimir_num_alunos(self):
        print(self.Num_Alunos)

    def imprimir_dias_aula(self):
        print(self.Dias_Aula)

    def imprimir_horario_aulas(self):
        print(self.Horario_Aulas)


def create_turma_from_db(ID_Turma):
    cursor = conexao.cursor()

    # Obter informações da turma
    command = f'SELECT ID_Disciplina, Num_Alunos, Dias_Aula, Horario_Aulas FROM Turma WHERE ID_Turma = {ID_Turma}'
    cursor.execute(command)
    ID_Disciplina, Num_Alunos, Dias_Aula, Horario_Aulas = cursor.fetchone()

    # Obter informações da disciplina
    command = f'SELECT Nome_Disciplina, Tipo, Periodo FROM Disciplina WHERE ID_Disciplina = {ID_Disciplina}'
    cursor.execute(command)
    Nome, Tipo, Periodo  = cursor.fetchone()


    # Criar objeto de turma
    turma = Turma(Nome, Tipo, Periodo, Num_Alunos, Dias_Aula, Horario_Aulas)

    cursor.close()
    return turma


turma = create_turma_from_db(5)
turma.imprimir_nome()
turma.imprimir_tipo()
turma.imprimir_periodo()
turma.imprimir_num_alunos()
turma.imprimir_dias_aula()
turma.imprimir_horario_aulas()
