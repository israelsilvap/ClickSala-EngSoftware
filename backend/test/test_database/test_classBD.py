import pytest
from database.classBD import BancoDeDados

def test_inserirLocal():
    bd = BancoDeDados()
    assert bd.inserirLocal("Sala Teste",50) == True