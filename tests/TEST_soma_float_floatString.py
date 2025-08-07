from functions.soma import *
def test_soma_float_floatString():
    a = "1.5"
    b = "1.5"
    resultadoEsperado = 4
    resultado = soma(a, b)
    assert resultado == resultadoEsperado