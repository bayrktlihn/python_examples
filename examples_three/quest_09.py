def whisper(text):
    before = " "
    result = ""
    for letter in text:
        if before.isspace() and letter.isalpha():
            result += letter
        elif before.isspace() and letter.isspace():
            result += letter
        before = letter
    return result.lower()


xx = "A L I H A N  B A Y R A K T A R !"

result = whisper(xx)

print(result)

