from functions.divide import *

def test_divide():
    a = 2
    b = 2
    resultado = divide(a, b)
    resultadoEsperado = 1
    assert resultado == resultadoEsperado