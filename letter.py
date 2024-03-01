def letters_count(file):
    
    # const
    vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы',
          'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']
    consonant = ['b', 'c', 'd', 'q', 'w', 'r', 't', 'p', 's', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'v', 'n',
             'm', 'й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч', 'с', 'м', 'т', 'б', 'ь', 'ъ']
    
    # var
    vowels_count = 0
    consonant_count = 0
    
    #main
    content = file.read()
    
    for i in content:
        if i in vowels:
            vowels_count += 1
        elif i in consonant:
            consonant_count += 1
  
    print("Vowels count: ", vowels_count)
    print("Consonant count: ", consonant_count)
