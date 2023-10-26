import mysql.connector

def get_db_connection():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password= '5991',
        database= 'bd_salas'
    )
    return conexao

def create_sala(CAPACIDADE):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO sala (CAPACIDADE) VALUES ({CAPACIDADE})'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def remove_sala(idSALA):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    command = f'DELETE FROM sala WHERE idSALA = {idSALA}'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def create_agenda(PHR, SHR, THR, QHR):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO agenda (PHR, SHR, THR, QHR) VALUES ({PHR}, {SHR}, {THR}, {QHR})'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def remove_agenda(idAGENDA):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    command = f'DELETE FROM agenda WHERE idAGENDA = {idAGENDA}'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def create_disciplina(PERIODO, CH, NOME, CARATER, TIPO):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO disciplina (PERIODO, CH, NOME, CARATER, TIPO) VALUES ({PERIODO}, {CH}, "{NOME}", "{CARATER}", "{TIPO}")'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def remove_disciplina(idDISCIPLINA):
    conexao = get_db_connection()
    
    cursor = conexao.cursor()
    
    command = f'DELETE FROM disciplina WHERE idDISCIPLINA = {idDISCIPLINA}'
    
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()



def create_turma(idDISCIPLINA, QUANT_ALUNOS):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO turma (idDISCIPLINA, QUANT_ALUNOS) VALUES ({idDISCIPLINA}, {QUANT_ALUNOS})'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

def remove_turma(idTURMA):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'DELETE FROM turma WHERE idTURMA = {idTURMA}'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()


def update_sala(idSALA, DIA,idAGENDA):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'UPDATE sala SET ({DIA}) = ({idAGENDA}) WHERE idSALA = {idSALA}'
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()
