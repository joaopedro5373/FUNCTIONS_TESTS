from functions.soma import *
def test_soma_emptyString():
    a="eqd"
    b="qedwe    dwe"
    resultadoEsperado = 0
    resultado = soma(a, b)
    assert resultado == resultadoEsperado