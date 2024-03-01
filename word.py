def word_count(file):
    content = file.read()
    words = content.split()
    print(f"Количество слов в файле: {len(words)}")
    
def most_common(file):
    content = file.read()
    words = content.split()
    word = {}
    for word in words:
        word[word] = word.get(word, 0) + 1
    sorted_words = sorted(word.items(), key=lambda x: x[1], reverse=True)
    print(f"Самые часто встречающиеся слова: {sorted_words[:5]}")