"""
Напишите функцию, которая возращает true, если число является простым
"""


def is_prime(n: int) -> bool:
    if n % 2 != 0 and n % 3 != 0:
        return True
    return False

assert is_prime(28)
assert not is_prime(23)
assert not is_prime(5)
print("Tests passed")
