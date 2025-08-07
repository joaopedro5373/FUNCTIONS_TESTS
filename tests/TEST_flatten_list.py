from functions.flatten_list import *

def test_flatten_list():
    objetos = ["mesa", "cama"]
    frutas = ["banana", "morango"]
    nested_list = [frutas, objetos]
    resultado = flatten_list(nested_list)
    resultadoEsperado = ["banana", "morango", "mesa", "cama"]
    assert resultado == resultadoEsperado