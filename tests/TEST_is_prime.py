from functions.is_prime import *

def test_is_prime():
    n = 3
    resultado = is_prime(n)
    resultadoEsperado = True
    assert resultado == resultadoEsperado