class FileProcessor:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, 'r') as file:
                self.content = file.read()

        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")



    def count_words(self):
        words = self.content.split()
        return len(words)

    def count_sentences(self):
        sentences = self.content.split('.')
        sentences.pop(-1)
        return len(sentences)

    def sort_words(self):
        word_count = {}
        words = self.content.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_words

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        vowel_count = 0
        for line in self.content:
            for char in line:
                if char.isalpha() and char.lower() in vowels:
                    vowel_count += 1
        return vowel_count

    def count_consonants(self):
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        consonant_count = 0
        for line in self.content:
            for char in line:
                if char.isalpha() and char.lower() in consonants:
                    consonant_count += 1
        return consonant_count