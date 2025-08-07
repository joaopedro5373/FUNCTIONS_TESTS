from functions.formatar_nome import *

def test_formatarNome():
    nome = "João"
    sobrenome = "Pedro"
    resultadoEsperado = "João Pedro"
    resultado = formatar_nome(nome, sobrenome)
    assert resultado == resultadoEsperado