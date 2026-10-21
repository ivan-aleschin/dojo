# Python 06 — Ввод-вывод, рекурсия и формат контеста

> 20 минут. Специфика отборочных экзаменов: там читают stdin, а не пишут функцию.

## Два разных формата задач

| Где | Что от тебя хотят |
|---|---|
| LeetCode, живая секция | написать **функцию** `def solve(nums, k) -> int` |
| Т-Банк / Яндекс.Контест / CodeRun | прочитать **stdin**, напечатать в **stdout** |

На отборочных экзаменах чаще второй формат. Ошибка чтения ввода = 0 баллов
при верном алгоритме. Поэтому шаблон должен быть в пальцах.

## Чтение ввода

```python
n = int(input())                        # одно число в строке
a, b = map(int, input().split())        # два числа через пробел
nums = list(map(int, input().split()))  # массив в одной строке
s = input().strip()                     # строка

# n строк
rows = [input().strip() for _ in range(n)]

# матрица n × m
grid = [list(map(int, input().split())) for _ in range(n)]
```

Когда данных много (10⁵ строк и больше), `input()` тормозит. Быстрый вариант:

```python
import sys
data = sys.stdin.read().split()   # весь ввод одним куском, список токенов
it = iter(data)
n = int(next(it))
nums = [int(next(it)) for _ in range(n)]
```

Или проще, если формат простой:

```python
import sys
input = sys.stdin.readline    # ускоряет input() в разы
```

⚠️ `sys.stdin.readline` **оставляет** `\n` в конце — для строк нужен `.strip()`.

Читать до конца ввода (когда количество строк не задано):

```python
import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    ...
```

## Вывод

```python
print(ans)
print(*nums)                  # элементы через пробел
print(" ".join(map(str, nums)))
print("\n".join(map(str, nums)))   # быстрее, чем print в цикле
print("YES" if ok else "NO")
```

Много строк вывода — собери и напечатай один раз, иначе `print` в цикле съест время:

```python
out = []
for ans in answers:
    out.append(str(ans))
sys.stdout.write("\n".join(out) + "\n")
```

## Шаблон решения контестной задачи

```python
import sys
from collections import Counter, defaultdict, deque
import heapq
import bisect


def solve() -> None:
    data = sys.stdin.read().split()
    it = iter(data)
    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    # ... алгоритм ...
    ans = 0

    print(ans)


if __name__ == "__main__":
    solve()
```

## Рекурсия

Лимит по умолчанию — 1000 вложенных вызовов. Глубокий DFS по дереву на 10⁵ узлов
упадёт с `RecursionError`. Первая строка при рекурсивном решении:

```python
import sys
sys.setrecursionlimit(300_000)
```

Если и это не спасает (Python-рекурсия ест много стека) — переписывай DFS
на явный стек:

```python
stack = [start]
visited = {start}
while stack:
    node = stack.pop()
    for nxt in graph[node]:
        if nxt not in visited:
            visited.add(nxt)
            stack.append(nxt)
```

## Замер и отладка

```python
print(f"{n=} {nums=}", file=sys.stderr)   # отладка в stderr — не портит ответ
```

На контесте это безопасно: проверяющая система смотрит только stdout.

## Формат этого репозитория: doctest

Задачи здесь оформляются как функции с примерами в docstring:

```python
def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Индексы двух чисел с суммой target.

    Время O(n), память O(n).

    >>> two_sum([2, 7, 11, 15], 9)
    (0, 1)
    >>> two_sum([3, 3], 6)
    (0, 1)
    """
    raise NotImplementedError
```

Запуск одного файла:

```
python -m doctest algorithms/two_pointers/02_valid_palindrome/solution.py -v
```

Весь репозиторий (pytest настроен на `--doctest-modules`):

```
pytest
```

Правила доктестов: ожидаемый вывод пишется **ровно так**, как его печатает
интерпретатор. Кортеж — `(0, 1)`, строка — `'abc'` в одинарных кавычках,
`True`/`False` с большой буквы. Пустая строка завершает пример.

## Мини-задачи

1. Прочитать `n`, затем `n` чисел, напечатать их сумму.
2. Прочитать матрицу `n × m` и напечатать её транспонированную.
3. Прочитать неизвестное число строк до EOF и напечатать количество непустых.
4. Написать функцию с доктестом и прогнать `python -m doctest`.
5. Почему `print` в цикле на 10⁵ итераций опасен на контесте?

<details><summary>Ответы</summary>

```python
1) n = int(input()); print(sum(map(int, input().split())))
2) grid = [list(map(int, input().split())) for _ in range(n)]
   for row in zip(*grid):
       print(*row)
3) print(sum(1 for line in sys.stdin if line.strip()))
5) каждый print — системный вызов с флашем; 10^5 вызовов дают секунды,
   а лимит обычно 1–2 с. Собрать в список и вывести одним join.
```
</details>
