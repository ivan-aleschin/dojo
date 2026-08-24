# Python 05 — Классы, узлы и типы

> 15 минут. Ровно столько ООП, сколько нужно для алгоритмических секций.

## Класс за 30 секунд

```python
class Stack:
    def __init__(self) -> None:      # конструктор, self — сам объект
        self._items: list[int] = []

    def push(self, x: int) -> None:
        self._items.append(x)

    def pop(self) -> int:
        if not self._items:
            raise IndexError("стек пуст")
        return self._items.pop()

    def __len__(self) -> int:        # теперь работает len(stack)
        return len(self._items)
```

`self` пишется явно первым аргументом в каждом методе. Подчёркивание `_items` —
соглашение «это внутреннее», приватности в Python нет.

Задачи типа **Min Stack**, **LRU Cache**, **Design HashMap**, «спроектируй очередь
на двух стеках» — это ровно про такой класс. На отборах они встречаются регулярно.

## Узел связного списка

Определение, которое надо уметь писать на автомате:

```python
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next
```

Обход и разворот:

```python
def to_list(head: ListNode | None) -> list[int]:
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

def reverse(head: ListNode | None) -> ListNode | None:
    prev = None
    cur = head
    while cur:
        nxt = cur.next     # запомнить, иначе потеряем хвост
        cur.next = prev    # развернуть ссылку
        prev = cur         # сдвинуть prev
        cur = nxt          # сдвинуть cur
    return prev
```

**Dummy-узел** — приём, который убирает половину edge-кейсов (удаление головы,
слияние списков):

```python
def merge(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next
```

## Узел дерева

```python
class TreeNode:
    def __init__(self, val: int = 0,
                 left: "TreeNode | None" = None,
                 right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right
```

Строим дерево для доктестов вручную:

```python
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
```

## dataclass — когда нужен просто контейнер данных

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)          # Point(x=1, y=2) — __repr__ бесплатно
p == Point(1, 2)  # True — __eq__ бесплатно
```

`@dataclass(frozen=True)` делает объект неизменяемым и хешируемым — его можно
класть в `set` и использовать как ключ словаря.

Для алгоритмических задач чаще достаточно кортежа `(x, y)`. `dataclass` бери,
когда полей больше трёх или нужны имена для читаемости.

## Аннотации типов (Python 3.14)

```python
def solve(nums: list[int], k: int) -> list[list[int]]: ...
def find(d: dict[str, int], key: str) -> int | None: ...
def walk(node: TreeNode | None) -> None: ...

from collections.abc import Iterable, Callable
def apply(xs: Iterable[int], f: Callable[[int], int]) -> list[int]: ...
```

Правила репо: `list[int]` вместо `List[int]`, `int | None` вместо `Optional[int]`.
Строка в кавычках (`"ListNode | None"`) нужна, когда тип ссылается сам на себя
внутри своего же определения.

## Магические методы, которые могут пригодиться

| Метод | Даёт |
|---|---|
| `__init__` | конструктор |
| `__repr__` | как объект печатается |
| `__len__` | `len(obj)` |
| `__eq__` | `==` |
| `__lt__` | `<`, а значит `sorted()` и работу в `heapq` |
| `__hash__` | возможность класть в `set`/`dict` |
| `__iter__` | `for x in obj` |

`__lt__` реально нужен, если кладёшь свои объекты в кучу. Проще — класть кортеж
`(приоритет, счётчик, объект)`.

## Мини-задачи

1. Написать класс `Queue` на двух списках так, чтобы `push` и `pop` были `O(1)` амортизированно.
2. Написать `ListNode` и функцию, собирающую связный список из `list[int]`.
3. Реализовать `MinStack`: `push`, `pop`, `top`, `get_min` — все за `O(1)`.
4. Сделать `@dataclass(frozen=True) Point` и положить набор точек в `set`.
5. Почему `def f(x, acc=[])` — плохая сигнатура? (ответ — в модуле 07)

<details><summary>Подсказка к №3</summary>

Держи второй стек с минимумами: при `push` кладёшь `min(x, текущий_минимум)`,
при `pop` снимаешь с обоих. Тогда `get_min` — это просто вершина второго стека.
</details>
