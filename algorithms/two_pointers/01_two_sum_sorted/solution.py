def two_sum_sorted(a: list[int], target: int) -> tuple[int, int]:
    """Индексы (1-based) двух чисел из ОТСОРТИРОВАННОГО массива с суммой target.

    Схема "навстречу": left растёт, right убывает. Массив отсортирован, поэтому
    направление сдвига однозначно приближает сумму к target.

    Время O(n), память O(1).

    >>> two_sum_sorted([2, 7, 11, 15], 9)
    (1, 2)
    >>> two_sum_sorted([2, 3, 4], 6)
    (1, 3)
    >>> two_sum_sorted([-1, 0], -1)
    (1, 2)
    """
    left, right = 0, len(a) - 1
    while left < right:
        s = a[left] + a[right]
        if s == target:
            return (left + 1, right + 1)
        if s < target:
            left += 1
        else:
            right -= 1
    raise ValueError("решение не найдено")
