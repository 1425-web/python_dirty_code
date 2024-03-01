def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
    return len(words)


def count_sentences(filename):
    with open(filename, 'r') as file:
        content = file.read()
        sentences = content.split('.')
        sentences.pop(-1)
    return len(sentences)


def sort_words(filename):
    with open(filename, 'r') as file:
        word_count = {}
        content = file.read()
        words = content.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_words


def count_vowels(filename):
    vowels = "aeiouAEIOU"


    vowel_count = 0

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    if char.lower() in vowels:
                        vowel_count += 1


    return vowel_count

def count_consonants(filename):

    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    consonant_count = 0
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    if  char.lower() in consonants:
                        consonant_count += 1

    return consonant_count