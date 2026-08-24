# Python 04 — Стандартная библиотека для алгоритмов

> 25 минут. Пять модулей, которые закрывают почти все задачи с собесов.

## collections.Counter — частоты

```python
from collections import Counter

c = Counter("aabbbc")          # Counter({'b': 3, 'a': 2, 'c': 1})
c = Counter([1, 1, 2])         # работает с любым итерируемым
c["z"]                         # 0, НЕ KeyError
c.most_common(2)               # [('b', 3), ('a', 2)]
c.most_common()[-1]            # самый редкий
list(c.elements())             # 'a','a','b','b','b','c'

Counter("abc") == Counter("cba")   # True → проверка анаграммы одной строкой
Counter("aab") - Counter("ab")     # Counter({'a': 1}) — вычитание, отрицательные отбрасываются
sum(c.values())                    # общее количество
```

Top-K частых: `[x for x, _ in Counter(nums).most_common(k)]`.

## collections.defaultdict — словарь со значением по умолчанию

```python
from collections import defaultdict

g = defaultdict(list)          # значение по умолчанию — пустой список
g[1].append(2)                 # ключа 1 не было — создался сам
g[1].append(3)                 # {1: [2, 3]}

cnt = defaultdict(int)         # по умолчанию 0
for x in nums:
    cnt[x] += 1

groups = defaultdict(list)
for w in words:
    groups[tuple(sorted(w))].append(w)   # группировка анаграмм
```

Список смежности графа — почти всегда `defaultdict(list)`.

> ⚠️ Побочный эффект: простое чтение `g[999]` **создаёт** ключ. Если это мешает —
> используй `g.get(999, [])`.

## collections.deque — очередь с двух концов

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)        # в конец,   O(1)
q.appendleft(0)    # в начало,  O(1)
q.pop()            # с конца,   O(1)
q.popleft()        # с начала,  O(1)  ← вот ради этого он и нужен
q[0]               # заглянуть, не снимая
while q: ...       # пока не пуста
```

**BFS всегда на `deque`.** `list.pop(0)` — это `O(n)`, и BFS на списке становится `O(n²)`.
Это прямой вопрос на собесе: «почему deque, а не list?»

Скелет BFS:

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    q = deque([start])
    dist = {start: 0}
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return dist
```

## heapq — куча (мин-куча)

Всегда **минимальная**: наверху самый маленький элемент.

```python
import heapq

h = []
heapq.heappush(h, 5)       # O(log n)
heapq.heappush(h, 1)
h[0]                       # 1 — минимум, посмотреть за O(1)
heapq.heappop(h)           # 1 — снять минимум, O(log n)

nums = [3, 1, 4]
heapq.heapify(nums)        # превратить список в кучу за O(n), НА МЕСТЕ
heapq.nlargest(3, nums)    # 3 самых больших
heapq.nsmallest(3, nums)
heapq.heappushpop(h, x)    # положить и снять минимум за один проход
heapq.heapreplace(h, x)    # снять минимум и положить x
```

**Макс-куча** делается через отрицание: кладём `-x`, при снятии берём `-heappop(h)`.

Кортежи в куче — сортировка по первому элементу:

```python
heapq.heappush(h, (dist, node))       # Дейкстра
heapq.heappush(h, (freq, word))       # Top-K
```

> ⚠️ Если первые элементы равны, Python сравнит вторые. Если вторые несравнимы
> (например, объекты) — `TypeError`. Спасение: добавить счётчик-разделитель
> `(priority, index, obj)`.

Идиома «K самых больших за `O(n log k)`»: держим мин-кучу размера k.

```python
h = []
for x in nums:
    heapq.heappush(h, x)
    if len(h) > k:
        heapq.heappop(h)     # выкидываем самый маленький
# в куче — k самых больших, h[0] — k-й по величине
```

## bisect — бинарный поиск в отсортированном

```python
import bisect

a = [1, 3, 3, 5, 7]
bisect.bisect_left(a, 3)    # 1 — первая позиция, куда можно вставить 3
bisect.bisect_right(a, 3)   # 3 — последняя такая позиция
bisect.insort(a, 4)         # вставить с сохранением порядка, O(n) на вставку
```

Практическое применение:

```python
# сколько элементов < x
bisect.bisect_left(a, x)
# сколько элементов == x
bisect.bisect_right(a, x) - bisect.bisect_left(a, x)
# есть ли x
i = bisect.bisect_left(a, x)
found = i < len(a) and a[i] == x
# первый элемент >= x
i = bisect.bisect_left(a, x)
```

Знание `bisect` экономит 10 минут на контесте, но на живой секции могут попросить
написать бинпоиск руками — уметь надо и то, и другое (см. [паттерн 04](../patterns/04_binary_search.md)).

## itertools — комбинаторика

```python
from itertools import permutations, combinations, product, accumulate, groupby

list(permutations([1,2,3]))          # все 6 перестановок
list(permutations([1,2,3], 2))       # по 2
list(combinations([1,2,3], 2))       # [(1,2), (1,3), (2,3)]
list(product([0,1], repeat=3))       # все 8 троек из 0/1
list(accumulate([1,2,3,4]))          # [1, 3, 6, 10] — префиксные суммы!
list(accumulate([3,1,4], max))       # [3, 3, 4] — префиксные максимумы
```

`accumulate` — готовые префиксные суммы для [паттерна 06](../patterns/06_prefix_sums.md).

> ⚠️ На собесе `permutations` для задачи «сгенерируй все перестановки» — не ответ.
> Хотят увидеть [backtracking](../patterns/11_backtracking_dp.md) руками.
> А вот в контесте, где важен только результат, — используй.

## functools.lru_cache — мемоизация в одну строку

```python
from functools import lru_cache

@lru_cache(maxsize=None)     # или @cache в 3.9+
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

Превращает экспоненциальную рекурсию в линейную. Аргументы обязаны быть хешируемыми
(кортежи, не списки). Это «динамика сверху вниз» бесплатно.

## Мини-задачи

1. Найти два самых частых слова в списке `words`.
2. Проверить, что `s` и `t` — анаграммы, одной строкой.
3. Построить список смежности из списка рёбер `[(1,2), (2,3)]` (неориентированный).
4. Найти 3-й по величине элемент массива через кучу за `O(n log k)`.
5. Посчитать, сколько чисел в отсортированном массиве попадают в отрезок `[lo, hi]`.

<details><summary>Ответы</summary>

```python
1) [w for w, _ in Counter(words).most_common(2)]
2) Counter(s) == Counter(t)
3) g = defaultdict(list)
   for u, v in edges:
       g[u].append(v); g[v].append(u)
4) h = []
   for x in nums:
       heapq.heappush(h, x)
       if len(h) > 3: heapq.heappop(h)
   ans = h[0]
5) bisect.bisect_right(a, hi) - bisect.bisect_left(a, lo)
```
</details>
