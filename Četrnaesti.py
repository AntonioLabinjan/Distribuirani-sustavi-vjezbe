def count_vowels_consonants(tekst):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    consonant_count = 0

    for char in tekst.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return {'vowels': vowel_count, 'consonants': consonant_count}


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(count_vowels_consonants(tekst))
