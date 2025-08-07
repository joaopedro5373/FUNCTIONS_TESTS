from functions.wordOccurrences import *
def test_count_word_occurrences():
    word = "batata"
    text = "batata é gostosa de todo jeito, batata frita, batata cozida, batata rústica, batata palha, " \
    "batata em salgadinho, batata no purê, enfim, batata é vida."
    resultadoEsperado = 8
    resultado = count_word_occurrences(text, word)
    assert resultado == resultadoEsperado