import word
import sentences
import letter
import file_class

print("Привет! Это плохо написанная программа.")

name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"

file = file_class.nfile(filename)
content = file.get_content()
sentence = file.get_sentences()
words = file.get_words()

word.word_count(words)
sentences.sentence_count(content, sentence)
word.most_common(words)
letter.letters_count(content)