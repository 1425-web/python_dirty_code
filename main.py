import hello
import workWithWords

hello.Hello()

filename = "sample.txt"
with open(filename, 'r') as file:
    content = file.read()
    words = content.split(' ')
try:
    workWithWords.Analis_slov(words)
    workWithWords.Analis_predloz(content)
    workWithWords.Analis_bukv(content)

except FileNotFoundError:

    print(f"Файл '{filename}' не найден.")
