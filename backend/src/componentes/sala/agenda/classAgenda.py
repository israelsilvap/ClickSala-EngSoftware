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
    def salvar_para_arquivo(self):
        # Inicializar uma lista para armazenar as linhas de texto
        linhas = []
        
        for horario, status in self.horarios.items():
            # Adicionar cada linha à lista
            linhas.append(f'{horario}: {status}')
        
        # Juntar todas as linhas em uma única string e retornar
        return '\n'.join(linhas)