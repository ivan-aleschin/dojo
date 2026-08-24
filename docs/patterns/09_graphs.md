# Паттерн 09 — Графы: BFS / DFS, топосорт, Дейкстра

> **Приоритет: технические секции.** Плюс задачи «на сетке» (матрица)
> регулярно встречаются на отборах — а это тот же граф.

## Идея простыми словами

Граф — вершины и связи. Матрица — тоже граф: клетка = вершина,
соседи по четырём сторонам = рёбра. Половина «графовых» задач с собесов
выглядит как задача про поле `grid`.

Правило выбора:
- **BFS** — кратчайший путь в **невзвешенном** графе, «за сколько шагов», «по слоям»;
- **DFS** — «дойти куда угодно», компоненты связности, поиск циклов, перебор путей;
- **Топосорт** — есть зависимости «A перед B»;
- **Дейкстра** — рёбра с **разными весами**.

## Представление графа

```python
from collections import defaultdict

# список смежности — стандарт
g = defaultdict(list)
for u, v in edges:
    g[u].append(v)
    g[v].append(u)        # вторая строка только для НЕориентированного

# сетка — соседи вычисляются
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
```

`visited` — обязательный элемент. Без него граф с циклом даёт бесконечный обход.
Для сетки часто вместо `visited` метят саму клетку (экономия памяти),
но это портит вход — уточняй, можно ли.

## Скелет BFS (кратчайший путь по числу шагов)

```python
from collections import deque

def bfs(start, graph) -> dict:
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in dist:          # dist работает и как visited
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return dist
```

**Критично:** помечать вершину посещённой надо **при добавлении в очередь**,
а не при снятии. Иначе одна и та же вершина попадёт в очередь много раз
и сложность взорвётся.

**Multi-source BFS** — кладём в очередь сразу все стартовые вершины.
Так решается Rotting Oranges, 01 Matrix, Walls and Gates. Приём стоит запомнить
отдельно: он превращает «для каждого источника запусти BFS» (`O(n²)`) в один проход.

```python
q = deque()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == SOURCE:
            q.append((r, c))
            dist[(r, c)] = 0
```

## Скелет DFS по сетке

```python
def num_islands(grid: list[list[str]]) -> int:
    """Количество островов из '1', связность по четырём сторонам.

    Время O(rows * cols), память O(rows * cols) на стек рекурсии в худшем случае.
    """
    rows, cols = len(grid), len(grid[0])

    def sink(r: int, c: int) -> None:
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != "1":
            return
        grid[r][c] = "0"                 # помечаем посещённой
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            sink(r + dr, c + dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count
```

На сетке 1000×1000 рекурсия упадёт по глубине → переписывать на стек
(см. [Python 06](../python/06_io_contest.md)). На собесе достаточно **назвать** этот риск.

## Топологическая сортировка (алгоритм Кана)

> Дано: «чтобы пройти курс B, надо сначала A». Вопрос: можно ли пройти все курсы
> (нет ли цикла) и в каком порядке.

```python
from collections import defaultdict, deque

def course_order(n: int, prerequisites: list[list[int]]) -> list[int]:
    """Топологический порядок или [] при наличии цикла.

    Время O(V + E), память O(V + E).
    """
    g = defaultdict(list)
    indegree = [0] * n
    for course, prereq in prerequisites:
        g[prereq].append(course)
        indegree[course] += 1

    q = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in g[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:       # все зависимости закрыты
                q.append(nxt)

    return order if len(order) == n else []
```

**Ключевая мысль:** `len(order) != n` означает цикл. Это и есть способ
детектировать цикл в ориентированном графе — так спрашивают в Course Schedule.

## Дейкстра (веса рёбер)

```python
import heapq

def dijkstra(start: int, graph: dict[int, list[tuple[int, int]]], n: int) -> list[float]:
    """Кратчайшие расстояния от start. graph[u] = [(вес, v), ...].

    Время O((V + E) log V), память O(V).
    """
    dist = [float("inf")] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:               # устаревшая запись — пропускаем
            continue
        for weight, nxt in graph[node]:
            nd = d + weight
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist
```

Строка `if d > dist[node]: continue` — обязательна: в куче накапливаются
устаревшие пары, удалять их оттуда нельзя.

⚠️ Дейкстра **не работает с отрицательными весами**. Это стандартный
уточняющий вопрос: «веса могут быть отрицательными?» При «да» — Беллман-Форд.

## Union-Find (система непересекающихся множеств)

Нужна для «сколько компонент», «есть ли цикл в неориентированном»,
«соединить аккаунты». Часто быстрее и короче DFS.

```python
class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # сжатие пути
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                    # уже вместе → нашли цикл
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True
```

Операции — почти `O(1)` (обратная функция Аккермана). На секции достаточно
сказать «практически константа».

## Типичные ошибки

1. **Помечают посещённым при снятии из очереди**, а не при добавлении.
2. **Нет `visited`** → зацикливание.
3. **`pop(0)` вместо `deque`** → `O(n²)`.
4. **Забыли добавить обратное ребро** в неориентированном графе.
5. **Выход за границы сетки** — проверка `0 <= r < rows and 0 <= c < cols`.
6. **DFS вместо BFS для кратчайшего пути** — DFS не даёт кратчайший.
7. **Дейкстра на графе с отрицательными весами.**
8. **Не проверили `len(order) == n`** после топосорта.

## Задачи

| # | Задача | Приём |
|---|---|---|
| 1 | **Flood Fill** (E) | DFS/BFS на сетке |
| 2 | **Number of Islands** (M) | DFS, компоненты — разобран |
| 3 | **Max Area of Island** (M) | DFS с возвратом размера |
| 4 | **Rotting Oranges** (M) | multi-source BFS |
| 5 | **01 Matrix** (M) | multi-source BFS |
| 6 | **Surrounded Regions** (M) | DFS с границы (инверсия задачи) |
| 7 | **Clone Graph** (M) | DFS + словарь оригинал→копия |
| 8 | **Course Schedule** (M) | топосорт, детект цикла |
| 9 | **Course Schedule II** (M) | топосорт, вернуть порядок |
| 10 | **Pacific Atlantic Water Flow** (M) | два обхода с границ |
| 11 | **Word Ladder** (H) | BFS по неявному графу слов |
| 12 | **Network Delay Time** (M) | Дейкстра |
| 13 | **Number of Provinces** (M) | Union-Find или DFS |
| 14 | **Cheapest Flights Within K Stops** (M) | BFS по слоям / Беллман-Форд |

№6 и №10 учат важному приёму: вместо «найти всё, что не касается границы»
проще запустить обход **с границы** и инвертировать результат.

## Чек-лист

- [ ] Строю список смежности за 20 секунд, не забывая обратное ребро.
- [ ] Пишу BFS и DFS по сетке наизусть, с проверкой границ.
- [ ] Знаю, почему `visited` ставится при добавлении в очередь.
- [ ] Умею multi-source BFS и понимаю, что он экономит.
- [ ] Пишу топосорт Кана и определяю цикл через длину порядка.
- [ ] Знаю ограничение Дейкстры и что делать при отрицательных весах.
- [ ] Решил задачи 1–10.
