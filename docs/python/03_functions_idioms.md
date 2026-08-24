# Python 03 — Функции и идиомы

> 20 минут. То, что делает код коротким и читаемым на собесе.

## Перебор по-питоновски

```python
for i in range(n): ...            # 0..n-1
for i in range(1, n): ...         # 1..n-1
for i in range(n - 1, -1, -1): ...# с конца к нулю
for x in nums: ...                # значения
for i, x in enumerate(nums): ...  # индекс + значение
for i, x in enumerate(nums, 1): ...# нумерация с 1
for a, b in zip(xs, ys): ...      # параллельно, до конца короткого
```

`enumerate` — почти всегда лучше, чем `for i in range(len(nums))`. Собеседующий это замечает.

Сравнить соседние элементы:

```python
for prev, cur in zip(nums, nums[1:]): ...
```

## Распаковка

```python
a, b = b, a                 # обмен без временной переменной
first, *rest = [1, 2, 3]    # first=1, rest=[2,3]
*init, last = [1, 2, 3]     # init=[1,2], last=3
x, y = point                # кортеж в переменные
```

Обход соседей клетки в матрице — базовая идиома для графов на сетке:

```python
for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...
```

Обрати внимание на `0 <= nr < rows` — цепочка сравнений, так пишут в Python.

## sorted(key=...) — главный рабочий инструмент

```python
sorted(nums)                          # по возрастанию
sorted(nums, reverse=True)            # по убыванию
sorted(words, key=len)                # по длине
sorted(words, key=lambda w: (len(w), w))       # по длине, потом по алфавиту
sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)
sorted(d.items(), key=lambda kv: -kv[1])       # по значению по убыванию
intervals.sort(key=lambda x: x[0])             # интервалы по левой границе
```

Сортировка **устойчивая**: равные элементы сохраняют исходный порядок.
Поэтому «сначала по одному, потом по другому» можно делать в два прохода,
но лучше одним `key=` с кортежем.

Трюк «по одному полю возрастание, по другому убывание» для чисел:
`key=lambda x: (x[0], -x[1])`.

## Функции

```python
def f(a: int, b: int = 2, *args, **kwargs) -> int:
    return a + b

def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    ...
```

Аннотации типов не проверяются в рантайме, но в этом репо включён `mypy strict` —
и на собесе они показывают аккуратность. Современный синтаксис: `list[int]`,
`dict[str, int]`, `int | None` (не `List`, не `Optional`).

Возврат нескольких значений — просто кортеж: `return lo, hi`.

## Вложенные функции и замыкания — как писать DFS

```python
def num_islands(grid: list[list[str]]) -> int:
    rows, cols = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)
    return count
```

Вложенная функция **видит** переменные внешней (`rows`, `cols`, `grid`) — не надо
таскать их аргументами. Но чтобы **присвоить** внешнюю переменную, нужен `nonlocal`:

```python
def diameter(root):
    best = 0

    def depth(node):
        nonlocal best          # без этого best внутри станет локальной
        if not node:
            return 0
        left, right = depth(node.left), depth(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    depth(root)
    return best
```

Альтернатива `nonlocal` — список из одного элемента (`best = [0]`, `best[0] = ...`).
`nonlocal` чище.

## Полезные встроенные

```python
any(x > 0 for x in nums)        # хотя бы один
all(x > 0 for x in nums)        # все
sum(nums)
max(nums, key=len)              # max тоже принимает key
map(int, input().split())       # применить функцию ко всем
reversed(nums)                  # итератор в обратном порядке
zip(*matrix)                    # транспонировать матрицу
```

Ложные значения (`falsy`): `0`, `""`, `[]`, `{}`, `set()`, `None`, `False`.
Отсюда идиома `if not nums:` вместо `if len(nums) == 0:`.

> ⚠️ Осторожно: `if not x:` для числа считает `0` пустым. Если `0` — валидное
> значение, пиши `if x is None:`.

## Мини-задачи

1. Найти индекс максимального элемента списка одной строкой.
2. Развернуть словарь `{"a": 1, "b": 2}` → `{1: "a", 2: "b"}`.
3. Отсортировать список слов по количеству уникальных букв, по убыванию.
4. Написать функцию `neighbors(r, c, rows, cols)`, возвращающую список валидных соседей.
5. Что напечатает код? Почему?
   ```python
   x = 5
   def f():
       x = 10
   f()
   print(x)
   ```

<details><summary>Ответы</summary>

```python
1) max(range(len(a)), key=lambda i: a[i])   # или a.index(max(a))
2) {v: k for k, v in d.items()}
3) sorted(words, key=lambda w: len(set(w)), reverse=True)
4) def neighbors(r, c, rows, cols):
       return [(r + dr, c + dc) for dr, dc in ((1,0), (-1,0), (0,1), (0,-1))
               if 0 <= r + dr < rows and 0 <= c + dc < cols]
5) 5 — присваивание внутри функции создаёт ЛОКАЛЬНУЮ переменную.
   Чтобы изменить внешнюю, нужен global (модульный уровень) или nonlocal (во вложенной).
```
</details>
