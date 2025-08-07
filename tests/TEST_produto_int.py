from functions.produto import *

def test_produto_int():
    a = 2.51
    b = 2
    resultadoEsperado = 6
    resultado = produto(a, b)
    assert resultado == resultadoEsperado