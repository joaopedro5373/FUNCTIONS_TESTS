from functions.soma import *

def test_soma_int():
    a = 10
    b = 15
    resultadoEsperado = 25
    resultado = soma(a, b)
    assert resultado == resultadoEsperado