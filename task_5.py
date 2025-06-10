"""
    Проверить, является ли строка с пробелами палиндромом (а роза упала на лапу азора).
    Упростим задачу, допуская, что cлова в предложении разделяются только одним пробелом.
"""


def is_palindrom(s: str) -> bool:
    res = []
    for elem in s:
        if elem != " ":
            res.append(elem)
    if len(res) % 2 == 0:
        length = len(res) // 2
        part_1 = res[:length]
        part_2 = res[length:]
        reversed_part_2 = part_2[::-1]
        if part_1 == reversed_part_2:
            return True
        return False
    else:
        length = len(res) // 2
        part_1 = res[:length]
        part_2 = res[length+1:]
        reserved_part_2 = part_2[::-1]
        if part_1 == reserved_part_2:
            return True
        return False

assert is_palindrom("ab cde dcb a")
assert is_palindrom("asd fgh jk kjh gfd sa")
assert not is_palindrom("qwr lkjh gfj c")
assert is_palindrom(" ")
print("Tests passed")