class work_with_text():
    def __init__(self, content):
        self.content = content
        
    def get_sentences(self):
        self.sentences = self.content.split('.')
        return self.sentences
    
    def get_words(self):
        self.words = self.content.split()
        return self.words