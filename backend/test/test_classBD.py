import pytest
from classBD import BancoDeDados

def test_singleton():
    bd1 = BancoDeDados.getInstance()
    bd2 = BancoDeDados.getInstance()
    assert bd1 is bd2

def test_inserirLocal():
    bd = BancoDeDados.getInstance()
    assert bd.inserirLocal('Sala Teste', 30) == True

def test_inserirDocente():
    bd = BancoDeDados.getInstance()
    assert bd.inserirDocente('Docente Teste', ['segunda', 'terça'], ['08h00_10h00', '10h00_12h00']) == True

def test_inserirDisciplina():
    bd = BancoDeDados.getInstance()
    assert bd.inserirDisciplina('Disciplina Teste', 'Obrigatoria', 1) == True

def test_inserirTurma():
    bd = BancoDeDados.getInstance()
    assert bd.inserirTurma('Disciplina Teste', 'Docente Teste', 30, 'segunda', '08h00_10h00') == True
