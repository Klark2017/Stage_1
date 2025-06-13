"""
    Дана ФИО, напишите функцию, которая выводит фамилию и инициалы через точку.
    Например: "Лермонтов Михаил Юрьевич" -> "Лермонтов М. Ю."
"""


def get_person_short_name(fio: str) -> str:
    words = fio.split()
    res = words[0] + " "
    for i in words[1:]:
        res += i[0] + "."
    return res
print(get_person_short_name("Лермонтов Михаил Юрьевич"))



