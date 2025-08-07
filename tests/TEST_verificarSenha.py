from functions.verificarSenha import *
def test_verificarSenha():
    senha = "pAo12w#@swq121"
    resultadoEsperado = True
    resultado = verificar_senha(senha)
    assert resultado == resultadoEsperado