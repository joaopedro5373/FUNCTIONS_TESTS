from functions.calculateAverage import *

def test_calculate_avarage():
    numbers = [2, 4, 6, 8]
    resultado = calculate_average(numbers)
    resultadoEsperado = 5
    assert resultado == resultadoEsperado