# import mysql.connector

# conexao = mysql.connector.connect(
#     # host='db4free.net',
#     # user='dnilson',
#     # password= 'mat495986',
#     # database= 'bdmat495986'

#     host='localhost',
#     user='root',
#     password= '5991',
#     database= 'mydatabase'
# )


# def inserirLocal(nome, capacidade):
#     cursor = conexao.cursor()
#     comando = f"CALL CreateSala('{nome}', {capacidade})"
#     cursor.execute(comando)
#     cursor.close()
    


# print(inserirLocal("Sala Teste", 50))

from classBD import BancoDeDados

bd = BancoDeDados()

print(bd.inserirLocal("Sala Teste",100))