import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '5991',
    database= 'mydatabase'
)

def create_sala(Nome, Capacidade):
    cursor = conexao.cursor()

    # Chamar a função armazenada CreateSala
    command = f"CALL CreateSala('{Nome}', {Capacidade})"
    cursor.execute(command)
    conexao.commit()

    cursor.close()
    conexao.close()

create_sala('Sala 101', 30)

