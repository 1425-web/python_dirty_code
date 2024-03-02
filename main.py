from txt_file_w import txt_file
from workng_w_txt import workng_wth_text


filename = input("Введите имя файла: ")
text = workng_wth_text(txt_file(filename=filename).get_content())

vowel_count, consonant_count = text.count_vowels_and_consonants()
print(f"Количество слов: ", len(text.get_words()))
print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
