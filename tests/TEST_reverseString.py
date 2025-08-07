from functions.reverseString import *
def test_reverse_string():
    s = "banana"
    resultado = reverse_string(s)
    resultadoEsperado = "ananab"
    assert resultado == resultadoEsperado