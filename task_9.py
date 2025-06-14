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
                if lst.index(i) == lst.index(k):
                    continue
                else:
                    cort = (i,k)
                    res.append(cort)
                    lst.remove(i)
                    lst.remove(k)
                    break




    return res
# print(get_pairs_number([1, 2, 4, 3, 5, 2, 6], 7))
print(get_pairs_number([1, 2, 4, 3, 5, 2, 3, 3, 1, 2], 6))

