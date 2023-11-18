import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '5991',
    database= 'mydatabase'
)

# CLASSE AGENDA
class Agenda:
    def __init__(self):
        self.horarios = {
            '08h00_10h00' : 'Livre',
            '10h00_12h00' : 'Livre',
            '13h30_15h30' : 'Livre',
            '15h30_17h30' : 'Livre',
        }

    def exibir_horarios(self):
        for horario, status in self.horarios.items():
            print(f'{horario}: {status}')

# CLASSE SALA
class Sala:
    def __init__(self, Nome, Capacidade):
        self.Nome = Nome
        self.Capacidade = Capacidade
        self.dias = {
            'segunda' : Agenda(),
            'terca'   : Agenda(),
            'quarta'  : Agenda(),
            'quinta'  : Agenda(),
            'sexta'   : Agenda()
        }

    def exibir_sala(self):
        print(f'Nome: {self.Nome}')
        print(f'Capacidade: {self.Capacidade}')
        for dia, agenda in self.dias.items():
            print(f'\nAgenda para {dia}:')
            agenda.exibir_horarios()



def save_sala_to_db(sala):
    cursor = conexao.cursor()

    # Para cada dia da semana, crie um novo registro na tabela Horarios e obtenha o ID
    ID_Horario = {}
    for dia in ['segunda', 'terca', 'quarta', 'quinta', 'sexta']:
        horario = sala.dias[dia].horarios
        command = f"INSERT INTO Horarios (08h00_10h00, 10h00_12h00, 13h30_15h30, 15h30_17h30) VALUES ('{horario['08h00_10h00']}', '{horario['10h00_12h00']}', '{horario['13h30_15h30']}', '{horario['15h30_17h30']}')"
        cursor.execute(command)
        ID_Horario[dia] = cursor.lastrowid

    # Crie um novo registro na tabela Agenda e obtenha o ID
    command = f"INSERT INTO Agenda (Segunda, Terca, Quarta, Quinta, Sexta) VALUES ({ID_Horario['segunda']}, {ID_Horario['terca']}, {ID_Horario['quarta']}, {ID_Horario['quinta']}, {ID_Horario['sexta']})"
    cursor.execute(command)
    ID_Agenda = cursor.lastrowid

    # Crie um novo registro na tabela Sala
    command = f"INSERT INTO Sala (Nome, Capacidade, ID_Agenda) VALUES ('{sala.Nome}', {sala.Capacidade}, {ID_Agenda})"
    cursor.execute(command)

    cursor.close()
    conexao.commit()

def update_sala_in_db(sala):
    cursor = conexao.cursor()

    # Obter o ID da sala
    command = f"SELECT ID_Sala FROM Sala WHERE Nome = '{sala.Nome}'"
    cursor.execute(command)
    ID_Sala = cursor.fetchone()[0]

    # Para cada dia da semana, obtenha o ID do registro Horarios correspondente e atualize-o
    for dia in ['Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta']:
        horario = sala.dias[dia].horarios

        # Obter o ID do registro Horarios
        command = f"SELECT {dia} FROM Agenda WHERE ID_Agenda = (SELECT ID_Agenda FROM Sala WHERE ID_Sala = {ID_Sala})"
        cursor.execute(command)
        ID_Horario = cursor.fetchone()[0]

        # Atualizar o registro Horarios
        command = f"UPDATE Horarios SET 08h00_10h00 = '{horario['08h00_10h00']}', 10h00_12h00 = '{horario['10h00_12h00']}', 13h30_15h30 = '{horario['13h30_15h30']}', 15h30_17h30 = '{horario['15h30_17h30']}' WHERE ID_Horario = {ID_Horario}"
        cursor.execute(command)

    # Atualizar o registro Sala
    command = f"UPDATE Sala SET Nome = '{sala.Nome}', Capacidade = {sala.Capacidade} WHERE ID_Sala = {ID_Sala}"
    cursor.execute(command)

    cursor.close()
    conexao.commit()



# Crie uma instância da classe Sala
sala = Sala('Sala 101', 30)

# Exiba as informações da sala
sala.exibir_sala()

save_sala_to_db(sala)