def fix_text(text):
    d = text.split(" ")
    y = [word for word in d if word != ""]

    return " ".join(y)


def find_index_begin_space(text: str):
    i = -1
    before_letter = " "

    for letter in text:
        i += 1
        if before_letter.isspace() and not letter.isspace():
            break
        before_letter = letter

    return i


def find_index_last_space(text: str):
    text = text[::-1]
    return (len(text) - 1) - find_index_begin_space(text)


def middlestrip(text: str):
    real_text = text.strip()
    real_text = fix_text(real_text)
    real_text = real_text.replace(" ", "")

    begin_index = find_index_begin_space(text)
    end_index = find_index_last_space(text)

    return text[0: begin_index] + real_text + text[end_index + 1:]


x = middlestrip("           alihan           batraktar          alid      ")
