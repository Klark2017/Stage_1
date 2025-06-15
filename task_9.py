"""
    Дан список целых чисел и определенное заданное число. Найти все пары из списка,
    сумма которых равна этому числу.
    Верните из функции список кортежей.
    Например: get_pairs_number([1, 2, 4, 3, 5, 2], 7) -> [(4,3), (5,2)]
"""


def get_pairs_number(lst: list[int], n) -> list[tuple]:
    res = []
    for i in lst:
        for k in lst[1:]:
            if i + k == n:
                 cort = (i,k)
                 res.append(cort)
                 lst.remove(i)
                 lst.remove(k)
                 break




    return res
print(get_pairs_number([1, 2, 4, 3, 5, 2, 6], 4))
print(get_pairs_number([1, 2, 4, 3, 5, 2, 3, 3, 3, 5, 1, 3, 3, 2], 6))

