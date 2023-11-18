import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '5991',
    database= 'mydatabase'
)


def create_turma(ID_Turma, ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horario_Aulas):
    cursor = conexao.cursor()

    # Verificar se o docente está disponível nos dias especificados
    command = f'SELECT Dia_Aula FROM Dias_Aula_Docente WHERE ID_Docente = {ID_Docente}'
    cursor.execute(command)
    dias_disponiveis = cursor.fetchall()
    print(dias_disponiveis)
    if Dias_Aula not in dias_disponiveis:
        print('O docente não está disponível nos dias especificados.')
        return

    # Verificar se o docente está disponível nos horários especificados
    command = f'SELECT Horario_Aula FROM Horarios_Aulas_Docente WHERE ID_Docente = {ID_Docente}'
    cursor.execute(command)
    horarios_disponiveis = cursor.fetchall()
    print(horarios_disponiveis)
    if Horario_Aulas not in horarios_disponiveis:
        print('O docente não está disponível nos horários especificados.')
        return

    # Se o docente estiver disponível, criar a turma
    command = f'INSERT INTO Turma (ID_Turma, ID_Disciplina, ID_Docente, Num_Alunos, Dias_Aula, Horario_Aulas) VALUES ({ID_Turma}, {ID_Disciplina}, {ID_Docente}, {Num_Alunos}, "{Dias_Aula}", "{Horario_Aulas}")'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()


create_turma(1, 1, 1, 30, 'segunda,quarta', '08:00-10:00')


# def create_sala(CAPACIDADE):
#     cursor = conexao.cursor()

#     command = f'INSERT INTO sala (CAPACIDADE) VALUES ({CAPACIDADE})'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# def remove_sala(idSALA):
#     cursor = conexao.cursor()
    
#     command = f'DELETE FROM sala WHERE idSALA = {idSALA}'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# def create_agenda(PHR, SHR, THR, QHR):
#     cursor = conexao.cursor()

#     command = f'INSERT INTO agenda (PHR, SHR, THR, QHR) VALUES ({PHR}, {SHR}, {THR}, {QHR})'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# def remove_agenda(idAGENDA):
#     cursor = conexao.cursor()
    
#     command = f'DELETE FROM agenda WHERE idAGENDA = {idAGENDA}'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# def create_disciplina(PERIODO, CH, NOME, CARATER, TIPO):
#     cursor = conexao.cursor()

#     command = f'INSERT INTO disciplina (PERIODO, CH, NOME, CARATER, TIPO) VALUES ({PERIODO}, {CH}, "{NOME}", "{CARATER}", "{TIPO}")'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# def remove_disciplina(idDISCIPLINA):
#     cursor = conexao.cursor()
    
#     command = f'DELETE FROM disciplina WHERE idDISCIPLINA = {idDISCIPLINA}'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()





# def remove_turma(idTURMA):
#     cursor = conexao.cursor()
    
#     command = f'DELETE FROM turma WHERE idTURMA = {idTURMA}'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()

# ##create_sala(45)
# #create_disciplina(7,64,'engenharia de software','obrigatoria','teorica')
# #create_turma(1,45)
# #remove_turma(22)
# #remove_disciplina(22)
# #remove_sala(3)


# # CRUD
# # READ

# #comando = f'SELECT * FROM vendas;'
# #cursor.execute(comando)
# #resultado = cursor.fetchall() # ler o banco de dados
# #print(resultado)

# #UPDATE

# def update_sala(idSALA, DIA,idAGENDA):
#     cursor = conexao.cursor()
    
#     command = f'UPDATE sala SET {DIA} = {idAGENDA} WHERE idSALA = {idSALA}'
#     cursor.execute(command)
#     conexao.commit()

#     cursor.close()
#     conexao.close()



# #create_disciplina(4, 64, "Banco de Dados", "Obrigatoria", "Opcional")
# #create_turma(2,30)
# #create_sala(45)

# update_sala(12,"SEG",1)

# #nome_produto = "todinho"
# #valor = 6
# #comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# #cursor.execute(comando)
# #conexao.commit()