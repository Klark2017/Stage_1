"""
Напишите функцию, которая возвращает true, если
три заданных числа (в указанном порядке) являются последовательными членами
арифметической прогрессии
"""


def is_arifm_progression(a: int, b: int, c: int) -> bool:
    if b - a == c - b:
        return True
    return False

assert is_arifm_progression(3, 6, 9)
assert not is_arifm_progression(3, 7, 9)
assert is_arifm_progression(20, 15, 10)
print("Tests passed")
