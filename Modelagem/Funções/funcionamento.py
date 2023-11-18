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
    def exibir_para_arquivo(self):
        # Inicializar uma lista para armazenar as linhas de texto
        linhas = []
        
        for horario, status in self.horarios.items():
            # Adicionar cada linha à lista
            linhas.append(f'{horario}: {status}')
        
        # Juntar todas as linhas em uma única string e retornar
        return '\n'.join(linhas)
            
    
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
        
    def is_available(self, Dias_Aula, Horario_Aulas):
        # Verificar se a sala está disponível nos dias e horários que a turma precisa
        for dia in Dias_Aula:
            for horario in Horario_Aulas:
                if self.dias[dia].horarios[horario] not in ['Livre', None]:
                    return False
        return True
    
    def allocate(self, turma):
        # Verificar se a sala está disponível
        if self.is_available(turma.Dias_Aula, turma.Horario_Aulas):
            # Alocar a turma na sala
            for dia in turma.Dias_Aula:
                for horario in turma.Horario_Aulas:
                    self.dias[dia].horarios[horario] = turma.Nome

    def exibir_sala(self):
        print(f'Nome: {self.Nome}')
        print(f'Capacidade: {self.Capacidade}')
        for dia, agenda in self.dias.items():
            print(f'\nAgenda para {dia}:')
            agenda.exibir_horarios()
    def gravar_sala_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, 'a') as f:
            f.write('------------------\n')
            f.write(f'Nome: {self.Nome}\n')
            f.write(f'Capacidade: {self.Capacidade}\n')
            for dia, agenda in self.dias.items():
                f.write(f'\nAgenda para {dia}:\n')
                # Supondo que `agenda.exibir_horarios()` retorna uma string
                f.write(agenda.exibir_para_arquivo() + '\n')



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

# ALOCAÇÃO
def alocar_turmas(turmas, salas):
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
                # Passar para a próxima turma
                break

# Criando uma lista de turmas
turmas = [create_turma_from_db(i) for i in range(1, 11)]

# Criando uma lista de salas
salas = [create_sala_from_db(i) for i in range(1, 6)]


for sala in salas:
    sala.exibir_sala()

print("\n\n################\n\n")

alocar_turmas(turmas, salas)

# for sala in salas:
#     sala.exibir_sala()

for sala in salas:
    sala.gravar_sala_em_arquivo('salas.txt')

