def fix_text(text):
    text = text.split()
    return " ".join(text)


def shout(text):
    result = ""
    text = fix_text(text).upper()
    for letter in text:
        if letter == " ":
            result += letter
        else:
            result += letter + " "
    result += "!"

    return result


print(shout(" \n\n\nalihan                                    bayraktar        "))
