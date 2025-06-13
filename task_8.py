"""
    Напишите функцию, которая вернет true, если список является полностью возрастающим,
    т.е. каждый следующий элемент больше предыдущего
"""


def is_list_growing(lst: list[float]) -> bool:
    val = lst[0]
    for elem in lst[1:]:
        if elem <= val:
            val = elem
            return False
    return True

print(is_list_growing([2, 8, 15, 92, 101]))
print(is_list_growing([2, 6, 0, 8, 9]))

