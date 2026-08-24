# python_drills — тренировка по Python

Сюда пишешь мини-задачи из модулей [`docs/python/`](../docs/python/01_basics_types.md).
Один модуль = один файл. Файл заранее заведён, в нём шапка со списком задач —
дописываешь решения прямо под ними.

| Файл | Модуль | Тема |
|---|---|---|
| `01_basics_types.py` | [01](../docs/python/01_basics_types.md) | числа, деление, строки, срезы |
| `02_collections.py` | [02](../docs/python/02_collections.md) | list / dict / set / tuple, comprehensions |
| `03_functions_idioms.py` | [03](../docs/python/03_functions_idioms.md) | enumerate, zip, sorted(key=), nonlocal |
| `04_stdlib_algo.py` | [04](../docs/python/04_stdlib_algo.md) | Counter, defaultdict, deque, heapq, bisect |
| `05_oop_and_typing.py` | [05](../docs/python/05_oop_and_typing.md) | классы, ListNode/TreeNode, dataclass |
| `06_io_contest.py` | [06](../docs/python/06_io_contest.md) | чтение stdin, шаблон контеста |
| `07_gotchas.py` | [07](../docs/python/07_gotchas.md) | грабли, самотест |
| `08_complexity.py` | [08](../docs/python/08_complexity.md) | оценка сложности вслух |

## Как работать

1. Читаешь модуль в `docs/python/`.
2. Открываешь соответствующий файл здесь и **набираешь решения руками** —
   не копипастом из урока. Смысл именно в моторике: на собесе автодополнения не будет.
3. Проверяешь себя: сначала решаешь, потом сверяешься со спойлером в модуле.

## Проверка

Пиши решения функциями с доктестами — тогда всё проверяется одной командой:

```python
def digits_only(s: str) -> str:
    """Оставить только цифры.

    >>> digits_only("a1b2c3")
    '123'
    """
    return "".join(c for c in s if c.isdigit())
```

```bash
pytest python_drills                     # все дрилы
python -m doctest python_drills/01_basics_types.py -v   # один файл
```

Файлы без доктестов тесты не ломают — пока не написал ни одного, `pytest` их просто пропускает.
