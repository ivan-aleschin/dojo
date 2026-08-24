# Паттерн 11 — Backtracking + Динамическое программирование

> **Приоритет: технические секции.** Самый большой урок — здесь два паттерна,
> и между ними прямая связь: DP — это backtracking, у которого научились
> не пересчитывать одно и то же дважды.

---

# Часть 1. Backtracking (перебор с возвратом)

## Идея простыми словами

Строим ответ по одному элементу. На каждом шаге пробуем все варианты:
взял вариант → пошёл вглубь → **вернул как было** → пробуем следующий.
Дерево решений обходится в глубину, «возврат» — это откат состояния.

Три вопроса, на которые нужно ответить перед кодом:

1. **Что такое состояние?** (текущий путь `path`, позиция `start`)
2. **Когда мы у цели?** (условие записи ответа)
3. **Какие варианты доступны из состояния?** (цикл `for`)

## Триггеры

- «все возможные», «перечислить», «сколько существует способов **и покажи какие**»;
- подмножества, перестановки, комбинации, расстановки;
- малое ограничение: `n ≤ 20` — прямая подсказка на экспоненту;
- судоку, N ферзей, поиск слова в матрице.

## Универсальный скелет

```python
def solve(...):
    res = []
    path = []

    def backtrack(start: int) -> None:
        if is_goal(path):
            res.append(path[:])        # КОПИЯ, не ссылка!
            return
        for i in range(start, n):
            if not is_valid(i):
                continue
            path.append(choice(i))     # 1. выбрали
            backtrack(i + 1)           # 2. пошли вглубь
            path.pop()                 # 3. откатили

    backtrack(0)
    return res
```

Три строки «выбрал — вглубь — откатил» — это весь паттерн.
`path[:]` — обязательно: без копии в ответе окажутся пустые списки,
потому что `path` мутируется дальше. Это ошибка №1 в теме.

## Три канонические задачи — выучить наизусть

**Подмножества (Subsets), `O(n · 2ⁿ)`**

```python
def subsets(nums: list[int]) -> list[list[int]]:
    """Все подмножества.

    >>> subsets([1, 2])
    [[], [1], [1, 2], [2]]
    """
    res: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        res.append(path[:])            # каждое состояние — уже ответ
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return res
```

**Перестановки (Permutations), `O(n · n!)`**

```python
def permute(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []
    path: list[int] = []
    used = [False] * len(nums)

    def backtrack() -> None:
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            backtrack()
            path.pop()
            used[i] = False            # откатываем ОБА изменения
    backtrack()
    return res
```

Разница с подмножествами: нет `start`, каждый раз перебираются все элементы,
поэтому нужен `used`.

**Комбинации с суммой (Combination Sum)** — элемент можно брать много раз,
поэтому рекурсия идёт в `i`, а не `i + 1`:

```python
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res, path = [], []

    def backtrack(start: int, remain: int) -> None:
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0:
            return                     # отсечение
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remain - candidates[i])   # i, НЕ i + 1
            path.pop()

    backtrack(0, target)
    return res
```

## Отсечения (pruning)

Отсечение — то, что превращает «работает на бумаге» в «проходит по времени».

- выйти раньше, если текущая сумма уже больше цели;
- отсортировать и `break`, когда дальше заведомо не подойдёт;
- пропускать дубликаты: `if i > start and nums[i] == nums[i-1]: continue`
  (перед этим массив обязательно отсортирован).

## Типичные ошибки backtracking

1. **`res.append(path)` без копии.**
2. **Забыт откат** (`path.pop()` или `used[i] = False`).
3. **`i + 1` вместо `i`** там, где элемент можно использовать повторно (и наоборот).
4. **Дубликаты не отсечены** при повторяющихся входных значениях.
5. **Нет базы рекурсии** → бесконечный спуск.

---

# Часть 2. Динамическое программирование

## Идея простыми словами

DP применим, когда:
1. задача разбивается на **подзадачи того же вида**;
2. подзадачи **повторяются** (иначе это просто рекурсия).

Тогда каждый ответ считается **один раз** и запоминается.

Два стиля — оба надо уметь:

**Сверху вниз (мемоизация)** — обычная рекурсия + кеш. Пишется быстрее,
ближе к «как думал».

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def climb(n: int) -> int:
    if n <= 2:
        return n
    return climb(n - 1) + climb(n - 2)
```

**Снизу вверх (таблица)** — цикл, заполняющий массив. Нет риска
`RecursionError`, легче ужать память.

```python
def climb(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    return b            # память O(1) вместо O(n)
```

## Как подойти к DP-задаче: четыре шага

1. **Что такое состояние?** — «`dp[i]` = ответ для первых `i` элементов»
   или «`dp[i][j]` = ответ для префиксов длины `i` и `j`».
2. **Переход** — как `dp[i]` выражается через меньшие.
3. **База** — `dp[0]`, `dp[1]`.
4. **Порядок обхода** — чтобы к моменту вычисления `dp[i]` всё нужное уже посчитано.

Проговорить эти четыре пункта вслух до кода — ровно то, что оценивают на секции.
Написать таблицу для маленького примера руками — лучший способ поймать переход.

## Пять базовых DP, закрывающих большинство задач

**1. Лестница / Фибоначчи** — `dp[i] = dp[i-1] + dp[i-2]`.
Отсюда: Climbing Stairs, Min Cost Climbing Stairs, Decode Ways.

**2. House Robber** — «взять или пропустить»:

```python
def rob(nums: list[int]) -> int:
    """Максимальная сумма без двух соседей подряд.

    Время O(n), память O(1).

    >>> rob([1, 2, 3, 1])
    4
    >>> rob([2, 7, 9, 3, 1])
    12
    """
    take, skip = 0, 0
    for x in nums:
        take, skip = skip + x, max(skip, take)
    return max(take, skip)
```

**3. Coin Change** — «неограниченный рюкзак»:

```python
def coin_change(coins: list[int], amount: int) -> int:
    """Минимум монет на сумму amount, или -1.

    Время O(amount * len(coins)), память O(amount).

    >>> coin_change([1, 2, 5], 11)
    3
    >>> coin_change([2], 3)
    -1
    """
    INF = float("inf")
    dp = [0] + [INF] * amount
    for target in range(1, amount + 1):
        for coin in coins:
            if coin <= target:
                dp[target] = min(dp[target], dp[target - coin] + 1)
    return -1 if dp[amount] == INF else int(dp[amount])
```

**4. LIS — наибольшая возрастающая подпоследовательность.**
Наивно `O(n²)`: `dp[i] = 1 + max(dp[j])` по всем `j < i` с `nums[j] < nums[i]`.
Оптимально `O(n log n)` через `bisect` — держим массив «минимальных хвостов»:

```python
import bisect

def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

`tails` — **не** сам ответ-последовательность, а только её длина. Про это спрашивают.

**5. Двумерная сетка** — Unique Paths, Minimum Path Sum:
`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`. Строку можно
переиспользовать → память `O(m)`.

## Разобранный эталон: Coin Change сверху вниз

Чтобы увидеть связь backtracking → DP, вот та же задача перебором с кешем:

```python
from functools import lru_cache

def coin_change_top_down(coins: list[int], amount: int) -> int:
    @lru_cache(maxsize=None)
    def best(remain: int) -> float:
        if remain == 0:
            return 0
        if remain < 0:
            return float("inf")
        return min((best(remain - c) + 1 for c in coins), default=float("inf"))

    ans = best(amount)
    return -1 if ans == float("inf") else int(ans)
```

Убери `@lru_cache` — получится чистый backtracking с экспоненциальным временем.
Добавь — станет `O(amount · len(coins))`. Это и есть вся разница между
двумя частями урока, и это лучший ответ на вопрос «а как ты пришёл к DP?».

## Типичные ошибки DP

1. **Неверно выбрано состояние** — если переход не выписывается, чаще всего
   виновато состояние, а не арифметика.
2. **Забыта база** или база противоречит переходу.
3. **Неправильный порядок обхода** — используем ещё не посчитанное.
4. **Не то возвращают**: `dp[n]` вместо `max(dp)` (в LIS через `dp` — именно `max`).
5. **`lru_cache` на нехешируемых аргументах** (список) → `TypeError`, нужен `tuple`.
6. **Не сказали про оптимизацию памяти** — почти в любой 1D-DP можно свести
   к двум переменным, и это стоит проговорить.

## Задачи

**Backtracking**

| # | Задача |
|---|---|
| 1 | **Subsets** (M) |
| 2 | **Combination Sum** (M) |
| 3 | **Permutations** (M) |
| 4 | **Generate Parentheses** (M) |
| 5 | **Letter Combinations of a Phone Number** (M) |
| 6 | **Word Search** (M) — backtracking на сетке |
| 7 | **Subsets II** / **Combination Sum II** (M) — пропуск дубликатов |
| 8 | **Palindrome Partitioning** (M) |
| 9 | **N-Queens** (H) — классика, знать идею |

**DP**

| # | Задача | Тип |
|---|---|---|
| 10 | **Climbing Stairs** (E) | лестница |
| 11 | **Min Cost Climbing Stairs** (E) | лестница со стоимостью |
| 12 | **House Robber** (M) | взять/пропустить — разобран |
| 13 | **House Robber II** (M) | кольцо → два запуска |
| 14 | **Coin Change** (M) | рюкзак — разобран |
| 15 | **Longest Increasing Subsequence** (M) | LIS, оба решения |
| 16 | **Unique Paths** (M) | 2D-сетка |
| 17 | **Minimum Path Sum** (M) | 2D-сетка |
| 18 | **Word Break** (M) | DP по строке + множество слов |
| 19 | **Longest Common Subsequence** (M) | 2D по двум строкам |
| 20 | **Partition Equal Subset Sum** (M) | рюкзак 0/1 |
| 21 | **Edit Distance** (H) | 2D, классика финалов |

Цель по объёму на этот паттерн — **не меньше 15 задач динамики**: DP —
единственная тема, где количество решённого прямо превращается в скорость
распознавания на собесе.

## Чек-лист

- [ ] Пишу скелет backtracking с тремя строками «выбрал — вглубь — откатил».
- [ ] Помню про `path[:]` и умею объяснить, почему без копии всё ломается.
- [ ] Знаю разницу `backtrack(i)` и `backtrack(i + 1)`.
- [ ] Формулирую состояние, переход, базу и порядок обхода **словами** до кода.
- [ ] Пишу оба стиля DP: мемоизация и таблица.
- [ ] Умею ужать 1D-DP до `O(1)` памяти.
- [ ] Объясняю LIS за `O(n log n)` и что хранит `tails`.
- [ ] Решил ≥ 15 задач динамики.
