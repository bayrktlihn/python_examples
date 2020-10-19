def whisper(text):
    text = text.strip()
    before = " "
    result = ""

    space_count = 1

    for letter in text:

        if letter.isspace():
            space_count += 1

        if before.isspace() and letter.isalpha():
            result += letter
            space_count = 0
        elif before.isspace() and letter.isspace() and space_count == 2:
            result += letter

        before = letter
    return result.lower()


xx = "A L I H A N  B A Y R A K T A R !"

result = whisper(xx)

print(result)
