import word
import sentences
import letter
import file_class

print("Привет! Это плохо написанная программа.")

name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")

file = file_class.work_with_text(content)
sentence = file.get_sentences()
words = file.get_words()

word_count = word.word_count(words)
sentence_count = sentences.sentence_count(content, sentence)
most_common_words = word.most_common(words)
letters_count = letter.letters_count(content)

print(f"Количество слов в файле: {word_count}")
print(f"Количество предложений в файле: {sentence_count}")
print(f"Самые часто встречающиеся слова: {most_common_words}")
print(f"В файле {letters_count[0]} гласных и {letters_count[1]} согласных")