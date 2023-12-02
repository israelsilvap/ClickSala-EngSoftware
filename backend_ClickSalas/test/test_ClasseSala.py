from ClasseSala   import Sala
from ClasseAgenda import Agenda
from ClasseTurma  import Turma

def test_criar_sala():
    sala = Sala("Sala 01", 15)
    assert sala.Nome == "Sala 01"
    assert sala.Capacidade == 15

    # Verifica se os objetos Agenda são do mesmo tipo e têm os mesmos valores
    assert all(isinstance(sala.dias[dia], Agenda) for dia in sala.dias)
    
    # Verificar os valores específicos
    assert all(sala.dias[dia].horarios == {'08h00_10h00': 'Livre', '10h00_12h00': 'Livre', '13h30_15h30': 'Livre', '15h30_17h30': 'Livre'} for dia in sala.dias)

def test_is_available():
    sala = Sala("Sala 101", 30)
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], ["08h00_10h00", "10h00_12h00"])
    assert sala.is_available(turma.Dias_Aula, turma.Horario_Aulas)

def test_allocate():
    sala = Sala("Sala 101", 30)
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], ["08h00_10h00", "10h00_12h00"])
    sala.allocate(turma)
    for dia in turma.Dias_Aula:
        for horario in turma.Horario_Aulas:
            assert sala.dias[dia].horarios[horario] == turma.Nome

def test_exibir_sala(mocker):
    sala = Sala("Sala 101", 30)
    mocker.patch('builtins.print')
    sala.exibir_sala()
    print.assert_any_call('Nome: Sala 101')
    print.assert_any_call('Capacidade: 30')