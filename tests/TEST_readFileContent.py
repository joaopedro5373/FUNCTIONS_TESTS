from functions.readFileContent import *

def test_read_file_content():
    path = "frutas.txt"
    resultado = read_file_content(path)
    resultadoEsperado = "banana"
    assert resultado == resultadoEsperado