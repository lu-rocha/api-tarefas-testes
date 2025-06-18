# test_calculadora.py
from calculadora import soma


def test_soma_dois_numeros_positivos():
    resultado = soma(2, 3)
    assert resultado == 5


def test_soma_numero_negativo():
    resultado = soma(-1, 1)
    assert resultado == 0


def test_soma_com_zero():
    resultado = soma(0, 5)
    assert resultado == 5
