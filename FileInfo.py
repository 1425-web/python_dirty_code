class F_Info():
    """информация файла"""

    def __init__(self, filename, words, sentences, repeatWords, vowels,
                 consonants):
        self.filename = filename
        self.words = words
        self.sentences = sentences
        self.repeatWords = repeatWords
        self.vowels = vowels
        self.consonants = consonants


def Cnt_words(content):
    """подсчёт слов"""
    return len(content.split())


def Cnt_sentences(content):
    """подсчёт предложений"""
    return len(content.split('.'))


def Repeat_words(content):
    """список часто повторяющихся слов"""
    words = content.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:5]


def Cnt_vowels(content):
    """подсчёт гласных"""
    vowels = "eyuioaEYUIOA"
    cnt = 0
    for symb in content:
        if symb in vowels: cnt += 1
    return cnt


def Cnt_consonants(content):
    """подсчёт согласных"""
    consonants = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
    cnt = 0
    for symb in content:
        if symb in consonants: cnt += 1
    return cnt
