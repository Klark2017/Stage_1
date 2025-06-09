"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:
    if a == b and b == c:
        return "равносторонний"
        print("равносторонний")
    elif a == b or b == c or c == a:
        return "равнобедренный"
        print("равнобедренный")
    else:
        return "обычный"
    print(get_triangle_kind(26, 26, 26))

get_triangle_kind(26, 26, 26)
get_triangle_kind(68, 95,43)
get_triangle_kind(45, 45, 40)
