import pytest
from classTurma import Turma

def test_criar_turma():
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    assert isinstance(turma, Turma)

def test_imprimir_nome(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_nome()
    captured = capsys.readouterr() # Captura tudo que foi impresso na saída padrão ou na saída de erro padrão
    assert captured.out.strip() == "Matematica"

def test_imprimir_tipo(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_tipo()
    captured = capsys.readouterr()
    assert captured.out.strip() == "obrigatoria"

def test_imprimir_periodo(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_periodo()
    captured = capsys.readouterr()
    assert captured.out.strip() == "5"

def test_imprimir_num_alunos(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_num_alunos()
    captured = capsys.readouterr()
    assert captured.out.strip() == '30'

def test_imprimir_dias_aula(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_dias_aula()
    captured = capsys.readouterr()
    assert captured.out.strip() == "['segunda', 'quarta', 'sexta']"

def test_imprimir_horario_aulas(capsys):
    turma = Turma("Matematica", "obrigatoria", 5, 30, ["segunda", "quarta", "sexta"], "08h00_10h00")
    turma.imprimir_horario_aulas()
    captured = capsys.readouterr()
    assert captured.out.strip() == "08h00_10h00"