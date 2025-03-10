"""
Этот алгоритм работает за время O(n log n)
Timsort — это гибридный алгоритм. Python реализует Timsort на уровне встроенного кода, поэтому он работает очень быстро,
Timsort минимизирует количество операций, обрабатывая маленькие и почти отсортированные массивы быстрее
за счет умных оптимизаций.

Почему это лучше?
Встроенный будет быстрее того, который мы напишем. Данный алгоритм проще чем разрабатывать свой алгоритм
"""


def sort_array(arr):
    return sorted(arr)


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sort_array(numbers)
print(sorted_numbers)