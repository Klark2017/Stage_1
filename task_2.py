"""
Напишите функцию, которая возращает true, если число является простым
"""


def is_prime(n: int) -> bool:
    for elem in range(2, n):
        if n % elem == 0:
            return False
    return True

assert not is_prime(28)
assert  is_prime(23)
assert  is_prime(5)
assert not is_prime(25)
print("Tests passed")
