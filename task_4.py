"""
    Напишите функцию, которая принимает три положительных числа и
    возвращает вид треугольника (равносторонний, равнобедренный, обычный).
"""


def get_triangle_kind(a: int, b: int, c: int) -> str:
    if a == b and b == c:
        triangle = "равносторонний"
        return triangle
    elif a == b or b == c or c == a:
        triangle = "равнобедренный"
        return triangle
    else:
        triangle = "обычный"
        return triangle

print(get_triangle_kind(26, 26, 26))
print(get_triangle_kind(68, 95,43))
print(get_triangle_kind(45, 45, 40))
