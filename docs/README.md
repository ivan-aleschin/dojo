# docs/ — планы и учебные материалы

Здесь лежит всё, кроме `README.md` и `CLAUDE.md` (они остались в корне репозитория).

**Планы и документы:**

| Файл | Что внутри |
|---|---|
| [`DAILY_PLAN.md`](DAILY_PLAN.md) | что делать каждый день: заявки, паттерны, симуляции, mock-собесы |
| [`PREP_PLAN.md`](PREP_PLAN.md) | стратегия, компании и дедлайны, режим дня, прогресс по паттернам |
| [`RESUME.md`](RESUME.md) | резюме |
| [`BACKEND_ROADMAP.md`](BACKEND_ROADMAP.md) | бэкенд-темы на поздние секции: SQL, FastAPI, системный дизайн |

**Курсы и справочники:** `python/`, `patterns/`, `templates/`, `companies/` — ниже.

## С чего начать

| Если тебе нужно | Иди сюда |
|---|---|
| понять, что делать сегодня | [`DAILY_PLAN.md`](DAILY_PLAN.md) |
| вспомнить Python перед алгоритмами (2 дня) | [`python/01_basics_types.md`](python/01_basics_types.md) |
| изучить паттерн и порешать по нему задачи | [`patterns/01_hash_map.md`](patterns/01_hash_map.md) |
| оформить задачу, конспект или mock-собес | [`templates/`](templates/README.md) |
| понять, куда подаваться и когда | [`companies/shortlist.md`](companies/shortlist.md) |
| стратегия, дедлайны, прогресс | [`PREP_PLAN.md`](PREP_PLAN.md) |
| подготовиться к секции про бэкенд | [`BACKEND_ROADMAP.md`](BACKEND_ROADMAP.md) |
| обновить резюме | [`RESUME.md`](RESUME.md) |

## 1. `python/` — экспресс-повторение Python (2 дня)

Восемь модулей. Задача — не «выучить питон», а вернуть в руки инструменты,
которыми решаются алгоритмические задачи. Каждый модуль: 15–25 минут чтения
+ мини-задачи, которые надо набрать руками (не копипастить).

| # | Модуль | О чём |
|---|---|---|
| 01 | [Базовые типы, строки, срезы](python/01_basics_types.md) | числа, деление, строки, f-строки, срезы |
| 02 | [Коллекции](python/02_collections.md) | list / dict / set / tuple, comprehensions |
| 03 | [Функции и идиомы](python/03_functions_idioms.md) | enumerate, zip, sorted(key=), распаковка, lambda |
| 04 | [Стандартная библиотека для алгоритмов](python/04_stdlib_algo.md) | collections, heapq, bisect, itertools, math |
| 05 | [Классы и типы](python/05_oop_and_typing.md) | class, dataclass, ListNode/TreeNode, аннотации |
| 06 | [Ввод-вывод и контест](python/06_io_contest.md) | input, sys.stdin, рекурсия, шаблон решения, doctest |
| 07 | [Грабли Python](python/07_gotchas.md) | мутабельные дефолты, копии, is vs ==, сортировка |
| 08 | [Сложность O(...)](python/08_complexity.md) | как считать и как называть вслух на собесе |

## 2. `patterns/` — 11 паттернов алгоритмов

Основной курс. Один паттерн = один учебный день. Структура каждого урока
одинаковая, чтобы мозг привык к формату:

1. **Идея простыми словами** — зачем паттерн существует.
2. **Триггеры** — по каким словам в условии его узнать.
3. **Скелет кода** — шаблон, который пишется «на автомате».
4. **Разобранный эталон** — одна задача целиком, с рассуждением.
5. **Типичные ошибки** — где заваливаются на собесе.
6. **Задачи** — по нарастанию, с пометкой актуальности.
7. **Чек-лист** — что должен уметь на выходе.

| # | Паттерн | Приоритет |
|---|---|---|
| 01 | [Hash Map / Set](patterns/01_hash_map.md) | отбор |
| 02 | [Two Pointers](patterns/02_two_pointers.md) | отбор |
| 03 | [Sliding Window](patterns/03_sliding_window.md) | отбор |
| 04 | [Binary Search](patterns/04_binary_search.md) | отбор |
| 05 | [Stack / Monotonic Stack](patterns/05_stack.md) | отбор |
| 06 | [Prefix Sums / Intervals](patterns/06_prefix_sums.md) | отбор |
| 07 | [Fast & Slow / Связные списки](patterns/07_fast_slow.md) | секции |
| 08 | [Деревья BFS/DFS](patterns/08_trees.md) | секции |
| 09 | [Графы BFS/DFS](patterns/09_graphs.md) | секции |
| 10 | [Heap / Top-K](patterns/10_heap_topk.md) | секции |
| 11 | [Backtracking + DP](patterns/11_backtracking_dp.md) | секции |

**«Отбор»** — то, что реально встречается в отборочных онлайн-экзаменах
(Т-Банк, Авито, МТС). **«Секции»** — живые технические собеседования после отбора.

## 3. `templates/` — заготовки

[`templates/README.md`](templates/README.md) — шаблоны задачи, эталона, стаба,
контестного решения (stdin→stdout), конспекта дня и бланка mock-собеса.
Копируешь и заполняешь, а не выдумываешь формат каждый раз.

## 4. `companies/` — куда подаваться

[`companies/shortlist.md`](companies/shortlist.md) — шорт-лист работодателей
с обоснованием под цель «переезд в Сербию через ~3 года».
[`companies/oriocs_list.md`](companies/oriocs_list.md) — полный список компаний
с договором о практике из ОРИОКС, разобранный по категориям.

## Как решать задачи

Задачи из уроков решаются в репозитории по конвенции
`algorithms/<паттерн>/<NN_имя>/solution.py`. Доктесты в docstring, проверка:

```
python -m doctest algorithms/<паттерн>/<NN_имя>/solution.py -v
```

Порядок работы над каждой задачей — как на собеседовании:
уточняющие вопросы → идея и `O()` вслух → код → доктест → разбор.
