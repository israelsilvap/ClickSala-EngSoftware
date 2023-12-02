import mysql.connector
from componentes.turma.turmaClass import Turma
from componentes.sala.salaClass   import Sala


conexao = mysql.connector.connect(
    host='db4free.net',
    user='dnilson',
    password= 'mat495986',
    database= 'bdmat495986'
)

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

# ACESSA O BANCO DE DADOS PARA OBTER AS INFORMAÇÕES
def create_sala_from_db(ID_Sala):
    cursor = conexao.cursor()

    # Obter informações da sala
    command = f'SELECT Nome, Capacidade, ID_Agenda FROM Sala WHERE ID_Sala = {ID_Sala}'
    cursor.execute(command)
    Nome, Capacidade, ID_Agenda = cursor.fetchone()

    # Obter informações da agenda
    command = f'SELECT Segunda, Terca, Quarta, Quinta, Sexta FROM Agenda WHERE ID_Agenda = {ID_Agenda}'
    cursor.execute(command)
    ID_Horario_Segunda, ID_Horario_Terca, ID_Horario_Quarta, ID_Horario_Quinta, ID_Horario_Sexta = cursor.fetchone()

    # Criar objeto de sala
    sala = Sala(Nome, Capacidade)

    # Para cada dia da semana, obter o horário correspondente e preencher a agenda da sala
    for dia, ID_Horario in zip(['segunda', 'terca', 'quarta', 'quinta', 'sexta'], [ID_Horario_Segunda, ID_Horario_Terca, ID_Horario_Quarta, ID_Horario_Quinta, ID_Horario_Sexta]):
        command = f'SELECT 08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30 FROM Horarios WHERE ID_Horario = {ID_Horario}'
        cursor.execute(command)
        horario = cursor.fetchone()
        
        sala.dias[dia].horarios = {
            '08h00_10h00' : horario[0],
            '10h00_12h00' : horario[1],
            '13h30_15h30' : horario[2],
            '15h30_17h30' : horario[3],
        }

    cursor.close()
    return sala

def update_sala_in_db(sala):
    cursor = conexao.cursor()

    # Obter o ID da sala
    command = f"SELECT ID_Sala FROM Sala WHERE Nome = '{sala.Nome}'"
    cursor.execute(command)
    ID_Sala = cursor.fetchone()[0]

    # Para cada dia da semana, obtenha o ID do registro Horarios correspondente e atualize-o
    for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
        horario = sala.dias[dia].horarios        

        dia = dia.capitalize()
        
        # Obter o ID do registro Horarios
        command = f"SELECT {dia} FROM Agenda WHERE ID_Agenda = (SELECT ID_Agenda FROM Sala WHERE ID_Sala = {ID_Sala})"
        command = command.replace("'None'", "NULL")
        cursor.execute(command)
        ID_Horario = cursor.fetchone()[0]

        # Atualizar o registro Horarios
        command = f"UPDATE Horarios SET 08h00_10h00 = '{horario['08h00_10h00']}', 10h00_12h00 = '{horario['10h00_12h00']}', 13h30_15h30 = '{horario['13h30_15h30']}', 15h30_17h30 = '{horario['15h30_17h30']}' WHERE ID_Horario = {ID_Horario}"
        command = command.replace("'None'", "NULL")
        cursor.execute(command)

    # Commit das alterações
    conexao.commit()