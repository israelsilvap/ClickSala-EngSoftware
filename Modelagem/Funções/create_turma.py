import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '5991',
    database= 'mydatabase'
)


def create_turma(ID_Turma, ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horarios_Aulas):
    cursor = conexao.cursor()

    # Verificar se o docente está disponível nos dias especificados
    command = f'SELECT Dias_Aula FROM Dias_Aula_Docente WHERE ID_Docente = {ID_Docente}'
    cursor.execute(command)
    dias_disponiveis = cursor.fetchall()
    dias_aula_set = set(Dias_Aula)
    if not any(dias_aula_set.issubset(dias) for dias, in dias_disponiveis):
        print('O docente não está disponível nos dias especificados.')
        return

    # Verificar se o docente está disponível nos horários especificados
    command = f'SELECT Horarios_Aula FROM Horarios_Aulas_Docente WHERE ID_Docente = {ID_Docente}'
    cursor.execute(command)
    horarios_disponiveis = cursor.fetchall()
    horario_aulas_set = set(Horarios_Aulas)
    if not any(horario_aulas_set.issubset(horarios) for horarios, in horarios_disponiveis):
        print('O docente não está disponível nos horários especificados.')
        return

    # Converter Dias_Aula e Horario_Aulas em strings
    Dias_Aula = ','.join(Dias_Aula)
    Horario_Aulas = ','.join(Horarios_Aulas)
    
    # Se o docente estiver disponível, criar a turma
    command = f'INSERT INTO Turma (ID_Turma, ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horario_Aulas) VALUES ({ID_Turma}, {ID_Disciplina}, {ID_Docente}, {Num_Alunos}, "{Dias_Aula}", "{Horario_Aulas}")'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()


create_turma(1, 1, 1, 30, ['segunda'], ['08h00_10h00'])
# create_turma(2, 1, 2, 30, ['terca'], ['15h30_17h30'])
