import file_tools

print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"
file = file_tools.FileProcessor(filename)

print(f"Количество слов в файле: {file.count_words()}")
print(f"Количество предложений в файле: {file.count_sentences()}")
print(f"Самые часто встречающиеся слова: {file.sort_words()}")
print(f"Количество гласных букв: {file.count_vowels()}")
print(f"Количество согласных букв: {file.count_consonants()}")
