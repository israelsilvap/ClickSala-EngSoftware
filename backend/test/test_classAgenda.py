from classAgenda import Agenda

def test_criar_agenda():
    agenda = Agenda()
    assert isinstance(agenda, Agenda)

def test_exibir_horarios(mocker):
    agenda = Agenda()
    mocker.patch('builtins.print')
    agenda.exibir_horarios()
    print.assert_any_call('08h00_10h00: Livre')
    print.assert_any_call('10h00_12h00: Livre')
    print.assert_any_call('13h30_15h30: Livre')
    print.assert_any_call('15h30_17h30: Livre')

