import word
import sentences
import letter

print("Привет! Это плохо написанная программа.")

name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        
        word.word_count(file)
        sentences.sentence_count(file)
        word.most_common(file)
        letter.letters_count(file)
        
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
