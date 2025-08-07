def count_word_occurrences(text:str, word:str)->int:
    return text.lower().split().count(word.lower())