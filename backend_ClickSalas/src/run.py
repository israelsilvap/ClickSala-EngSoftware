import AcessoBancoDeDados as AcBd
from utilitarios.algoritmoAlocacao import alocar_turmas

# Criando uma lista de turmas
turmas = AcBd.create_turma_from_db()

# Criando uma lista de salas
salas = AcBd.create_sala_from_db()

# for sala in salas:
#     sala.exibir_sala()

print("\n\n---------------\n\n")

salas[1].exibir_sala()

alocar_turmas(turmas, salas)
    
for sala in salas:
    AcBd.update_sala_in_db(sala)
