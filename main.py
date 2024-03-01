import file_tools
print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        print(f"Количество слов в файле: {file_tools.count_words(filename)}")
        print(f"Количество предложений в файле: {file_tools.count_sentences(filename)}")
        print(f"Самые часто встречающиеся слова: {file_tools.sort_words(filename)}")
        print(f"Количество гласных букв: {file_tools.count_vowels(filename)}")
        print(f"Количество согласных букв: {file_tools.count_consonants(filename)}")
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
