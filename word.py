def word_count(words):
    print(f"Количество слов в файле: {len(words)}")
    
def most_common(words):
    word_c = {}
    for word in words:
        word_c[word] = word_c.get(word, 0) + 1
    sorted_words = sorted(word_c.items(), key=lambda x: x[1], reverse=True)
    print(f"Самые часто встречающиеся слова: {sorted_words[:5]}")