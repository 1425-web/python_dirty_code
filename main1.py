import hello
import workWithWords

hello.Hello()

filename = "sample.txt"

try:

    workWithWords.Analis(filename)

except FileNotFoundError:

    print(f"Файл '{filename}' не найден.")
