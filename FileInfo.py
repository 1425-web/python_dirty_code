class F_Info():
    """информация файла"""

    def __init__(self, words, sentences, repeatWords, vowels, consonants):
        self.words = words
        self.sentences = sentences
        self.repeatWords = repeatWords
        self.vowels = vowels
        self.consonants = consonants


def CntWords(filename):
    """подсчёт слов"""
    with open(filename, 'r') as file:
        return len(file.read().split())


def CntSentences(filename):
    """подсчёт предложений"""
    with open(filename, 'r') as file:
        return len(file.read().split('.'))


def RepeatWords(filename):
    """список часто повторяющихся слов"""
    with open(filename, 'r') as file:
        words = file.read().split()
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        sorted_words = sorted(word_count.items(),
                              key=lambda x: x[1],
                              reverse=True)
        return sorted_words[:5]


def Cnt_Vowels(filename):
    vowels = "eyuioaEYUIOA"
    cnt = 0
    with open(filename, 'r') as file:
        symbs = file.read()
        for symb in symbs:
            if symb in vowels: cnt += 1
    return cnt


def Cnt_Consonants(filename):
    consonants = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
    cnt = 0
    with open(filename, 'r') as file:
        symbs = file.read()
        for symb in symbs:
            if symb in consonants: cnt += 1
    return cnt
