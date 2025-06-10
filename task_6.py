"""
    Дана строка, разбить ее на слова. Слова разделены одним пробелом
    "Александр Сергеевич Пушкин" -> ["Александр", "Сергеевич", "Пушкин"]
"""


def get_words(s: str) -> list[str]:
    word = ""
    str = []
    for elem in s:
        if elem != " ":
            word += elem
        else:
            str.append(word)
            word = ""
    str.append(word)
    return str

print(get_words("asd yuik pu"))
print(get_words("Александр Сергеевич Пушкин"))