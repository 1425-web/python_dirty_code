def sentence_count(file):
    content = file.read()
    sentences = content.split('.')
    print(f"Количество предложений в файле: {len(sentences)}")