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