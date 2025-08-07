from functions.produto import *
def test_produto_string():
    a = "2"
    b = "7"
    resultadoEsperado = 14
    resultado = produto(a, b)
    assert resultado == resultadoEsperado