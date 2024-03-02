
class workng_wth_text:

    def count_vowels_and_consonants(self):
        vowels = "аеёиоуыэюя"
        consonants = "бвгджзйклмнпрстфхцчшщ"

        vowel_count = sum(1 for char in self.content if char.lower() in vowels)
        consonant_count = sum(1 for char in self.content if char.lower() in consonants)

        return vowel_count, consonant_count

    def __init__(self,content):
        self.content = content
        

    def get_words(self):
        return self.content.split()
        
    def get_sentences(self):
        return self.content.split('.')
        
    def get_sort_word(self):
        for word in self.get_words():
            word_count[word] = word_count.get(word, 0) + 1
        return sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
