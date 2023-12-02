import mysql.connector
import pandas as pd
import numpy as np

def get_db_connection():
    conexao = mysql.connector.connect(
        host='db4free.net',
        user='dnilson',
        password= 'mat495986',
        database= 'bdmat495986'
    )
    return conexao

# Função para atualizar o banco de dados a partir de um arquivo
def update_database_from_csv(file_path, table_name):
    # Ler os dados do arquivo .csv
    data = pd.read_csv(file_path, header=None)

    # Conectar ao banco de dados
    conexao = get_db_connection()
    cursor = conexao.cursor()

    # Limpar a tabela existente
    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    cursor.execute(f"TRUNCATE TABLE {table_name}")
    cursor.execute("SET FOREIGN_KEY_CHECKS=1")

    # Inserir os novos dados na tabela
    for i, row in data.iterrows():
        values = ', '.join([f'"{item}"' if pd.notnull(item) else 'NULL' for item in row])
        sql = f"INSERT INTO {table_name} VALUES ({values})"
        cursor.execute(sql)

    # Commit das alterações e fechar a conexão
    conexao.commit()
    cursor.close()
    conexao.close()

# Função para atualizar o arquivo a partir do banco de dados
def update_csv_from_database(file_path, table_name):
    # Conectar ao banco de dados
    conexao = get_db_connection()
    cursor = conexao.cursor()

    # Executar a consulta para obter todos os dados da tabela
    cursor.execute(f"SELECT * FROM {table_name}")

    # Escrever os resultados no arquivo .csv
    with open(file_path, 'w') as f:
        for row in cursor:
            f.write(','.join([str(item) for item in row]) + '\n')

    # Fechar a conexão
    cursor.close()
    conexao.close()

def create_sala(idSALA, CAPACIDADE):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO sala (idSALA, CAPACIDADE) VALUES ({idSALA},{CAPACIDADE})'
    cursor.execute(command)
    conexao.commit()
    
    cursor.close()
    conexao.close()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\sala.csv', 'sala')
    
def remove_sala(idSALA):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    command = f'DELETE FROM sala WHERE idSALA = {idSALA}'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\sala.csv', 'sala')
    
    cursor.close()
    conexao.close()

def update_sala(idSALA, CAPACIDADE):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'UPDATE sala SET CAPACIDADE = {CAPACIDADE} WHERE idSALA = {idSALA}'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\sala.csv', 'sala')
    
    cursor.close()
    conexao.close()

def create_agenda(idSALA, idTURMA, DIA_DA_SEMANA, HORARIO):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO agenda (idSALA, idTURMA, DIA_DA_SEMANA, HORARIO) VALUES ({idSALA}, {idTURMA}, {DIA_DA_SEMANA}, {HORARIO})'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv', 'agenda')

    cursor.close()
    conexao.close()

def remove_agenda(idAGENDA):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    
    command = f'DELETE FROM agenda WHERE idAGENDA = {idAGENDA}'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\agenda.csv', 'agenda')

    cursor.close()
    conexao.close()

def create_disciplina(idDISCIPLINA, PERIODO, CH, NOME, CARATER, TIPO):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO disciplina (idDISCIPLINA, PERIODO, CH, NOME, CARATER, TIPO) VALUES ({idDISCIPLINA}, {PERIODO}, {CH}, "{NOME}", "{CARATER}", "{TIPO}")'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\disciplina.csv', 'disciplina')

    cursor.close()
    conexao.close()

def remove_disciplina(idDISCIPLINA):
    conexao = get_db_connection()
    
    cursor = conexao.cursor()
    
    command = f'DELETE FROM disciplina WHERE idDISCIPLINA = {idDISCIPLINA}'
    
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\disciplina.csv', 'disciplina')

    cursor.close()
    conexao.close()

def create_turma(idTURMA, idDISCIPLINA, QUANT_ALUNOS):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'INSERT INTO turma (idTURMA, idDISCIPLINA, QUANT_ALUNOS) VALUES ({idTURMA}, {idDISCIPLINA}, {QUANT_ALUNOS})'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\turma.csv', 'turma')

    cursor.close()
    conexao.close()

def remove_turma(idTURMA):
    conexao = get_db_connection()
    cursor = conexao.cursor()

    command = f'DELETE FROM turma WHERE idTURMA = {idTURMA}'
    cursor.execute(command)
    conexao.commit()
    update_csv_from_database('C:\\Users\\Israel Silva\\Downloads\\engSoftw-TestesAPI\\arquivos_base\\turma.csv', 'turma')

    cursor.close()
    conexao.close()
