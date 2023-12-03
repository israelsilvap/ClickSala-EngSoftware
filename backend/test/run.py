import AcessoBancoDeDados as AcBd

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
turmas = [AcBd.create_turma_from_db(i) for i in range(1, 11)]

# Criando uma lista de salas
salas = [AcBd.create_sala_from_db(i) for i in range(1, 6)]

for sala in salas:
    sala.exibir_sala()

print("\n\n---------------\n\n")
    
for sala in salas:
    AcBd.update_sala_in_db(sala)