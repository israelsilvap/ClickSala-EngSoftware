from classBD import BancoDeDados

bd = BancoDeDados()

# bd.inserirLocal('Sala 101',30)

print(bd.inserirDocente('Elmano',['segunda', 'quarta','sexta'],['08h00_10h00','08h00_10h00,10h00_12h00','08h00_10h00,10h00_12h00']))
print(bd.inserirDocente('Jermana',['quinta', 'terca'],['10h00_12h00', '10h00_12h00']))
print(bd.inserirDisciplina('Calculo 1', 'optativa', 1))
print(bd.inserirDisciplina('ELETROMAGNETISMO APLICADO', 'obrigatoria', 4))
print(bd.get_ID_Disciplina('Calculo 1'))
print(bd.get_ID_Docente('Jermana'))
print(bd.inserirTurma('ELETROMAGNETISMO APLICADO','Elmano',45,'segunda,quarta,sexta','08h00_10h00'))
bd.inserirLocal("Sala 01",50)
bd.inserirLocal("Sala 02",50)
