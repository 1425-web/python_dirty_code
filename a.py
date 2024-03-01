from main import filee


def count_vowels_and_consonants(sentence):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"

    vowel_count = sum(1 for char in sentence if char.lower() in vowels)
    consonant_count = sum(1 for char in sentence if char.lower() in consonants)

    return vowel_count, consonant_count


filename = input("Введите имя файла: ")
file = filee(filename=filename)

vowel_count, consonant_count = count_vowels_and_consonants(
    sentence=file.content)
print(f"Количество слов: ", len(file.words))
print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
