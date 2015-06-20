def anti_vowel(text):
    no_vowels=""
    print no_vowels
    for char in text:
        if not isVowel(char):
            print char
            no_vowels+=char
    print no_vowels
    return no_vowels

def isVowel(char):
    char=char.lower()
    if char in ('a' or 'e' or 'i' or 'o' or 'u'):
        print True
        return True

anti_vowel("Hey look Words!")
