import FileInfo

print("Привет! Это плохо написанная программа.")
name = input("Введите ваше имя: ")
print(f"Привет, {name}!")

filename = "sample.txt"
try:
    open(filename, 'r')
    File1 = FileInfo.F_Info(FileInfo.CntWords(filename),
                            FileInfo.CntSentences(filename),
                            FileInfo.RepeatWords(filename))
    print(f"Количество слов в файле: {File1.words}")
    print(f"Количество предложений в файле: {File1.sentences}")
    print(f"Самые часто встречающиеся слова: {File1.repeatWords}")
except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
