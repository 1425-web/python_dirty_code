class nfile():
    def __init__(self,filename):
        try:
            with open(filename, 'r') as file:
                self.content = file.read().lower()
                self.sentences = self.content.split('.')
                self.words = self.content.split()
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден.")
    def get_content(self):
        return self.content
    def get_sentences(self):
        return self.sentences
    def get_words(self):
        return self.words