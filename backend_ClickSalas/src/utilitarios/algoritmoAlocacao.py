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