import random;
import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

words = ["ıRmak","ALİHAN","aeiıuüoö","AEİIUÜOÖ","  ÖMeR","KAZIM","  merve  ","DENİZ  ","ahmet","İLKNUR","ÜnAL", "  TEST   Aeeww  "]

vowels = ["e","i","ü","ö"]

consonant = ["a","ı","o", "u"]

word = words[random.randint(0, len(words) - 1)].strip()

numVowels = 0
numConsonant = 0

print("Selected",word)

for letter in word:
    if letter == 'I':
        letter = "ı"
    elif letter == 'İ':
        letter = "i"
    else:
        letter = letter.lower()

    if letter in vowels:
        numVowels += 1
    elif letter in consonant:
        numConsonant += 1

print("Number of vowels",numVowels)
print("Number of consonant", numConsonant)