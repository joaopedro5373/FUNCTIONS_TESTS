from functions.authenticate_user import *
def test_authenticate_user():
    username = "admin"
    password = "1234"
    resultado = authenticate_user(username, password)
    resultadoEsperado = True
    assert resultado == resultadoEsperado