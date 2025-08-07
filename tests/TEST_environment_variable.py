from functions.environment_variable import *

def test_environment_variable():
    os.environ["comida"] = "batata"
    resultadoEsperado = "batata"
    resultado = get_environment_variable("comida")
    assert resultado == resultadoEsperado