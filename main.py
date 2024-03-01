
def get_txt(filename):
    content = ''
    with open(filename, 'r') as file:
        content = file.read()
    return content


def split(str):
    return str.split


class filee:
    content = ''
    words = []
    sentences = []
    word_count = {}
    sorted_words = []

    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.content = file.read()
            self.words = self.content.split()
            self.sentences = self.content.split('.')
            for word in self.words:
                self.word_count[word] = self.word_count.get(word, 0) + 1
            self.sorted_words = sorted(
                self.word_count.items(), key=lambda x: x[1], reverse=True)

    def get_words(self):
        return self.words

    def get_sentences(self):
        return self.sentences

    def get_word_count(self):
        return self.word_count

    def get_soretd_words(self):
        return self.sorted_words

    def set_words(self, s):
        self.words = s

    def set_sentences(self, s):
        self.sentences = s

    def set_word_count(self, s):
        self.word_count = s

    def set_soretd_words(self, s):
        self.sorted_words = s
