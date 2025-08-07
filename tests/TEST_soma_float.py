from functions.soma import *

def test_soma_float():
    a = 0.55
    b = 0.25
    resultadoEsperado = 1
    resultado = soma(a, b)
    assert resultado == resultadoEsperado