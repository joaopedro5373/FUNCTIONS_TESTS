from functions.fatorial import *
def test_fatorial():
    numero = 3
    resultado = factorial(numero)
    resultadoEsperado = 6
    assert resultado == resultadoEsperado