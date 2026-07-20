# DAILY_PLAN — подготовка по дням (старт 20 июля 2026, Пн)

Формат дня и чек-листы итогов — в `PREP_PLAN.md`. Здесь — что именно делать каждый день.
`(E)` = easy, `(M)` = medium, `[stretch]` = по желанию, если осталось время.
Задачи ищи по названию на LeetCode или бери у меня в репо — я готовлю стабы.

Каждая задача: сначала уточнения → идея и `O()` вслух → код → доктест → разбор со мной.

---

## Фаза 1 — Фундамент паттернов (20 июля → 4 августа)

### Неделя 1

**День 1 — Пн 20.07 · Two Pointers · 6 задач**
Python: срезы, два индекса, `while left < right`.
1. Two Sum II (sorted) (E) — *эталон уже в репо*
2. Valid Palindrome (E) — *твоя первая задача*
3. Reverse String (E)
4. Remove Duplicates from Sorted Array (E)
5. Squares of a Sorted Array (E)
6. Container With Most Water (M)

**День 2 — Вт 21.07 · Sliding Window · 6 задач**
Python: `dict`/`Counter`, `set`, движущееся окно.
1. Maximum Average Subarray I (E)
2. Contains Duplicate II (E)
3. Longest Substring Without Repeating Characters (M)
4. Minimum Size Subarray Sum (M)
5. Max Consecutive Ones III (M)
6. Longest Repeating Character Replacement (M)

**День 3 — Ср 22.07 · Hash Map / Set · 6 задач**
Python: `defaultdict`, `Counter`, `set`.
1. Two Sum (E)
2. Contains Duplicate (E)
3. Valid Anagram (E)
4. Group Anagrams (M)
5. Top K Frequent Elements (M)
6. Longest Consecutive Sequence (M)

**День 4 — Чт 23.07 · Binary Search · 6 задач**
Python: `bisect`, инвариант `[lo, hi]`.
1. Binary Search (E)
2. Search Insert Position (E)
3. First Bad Version (E)
4. Find First and Last Position of Element (M)
5. Search in Rotated Sorted Array (M)
6. Koko Eating Bananas (M) — бинпоиск по ответу

**День 5 — Пт 24.07 · Stack / Monotonic Stack · 6 задач**
Python: `list` как стек, монотонный стек.
1. Valid Parentheses (E)
2. Next Greater Element I (E)
3. Min Stack (M)
4. Evaluate Reverse Polish Notation (M)
5. Daily Temperatures (M) — монотонный стек
6. Car Fleet (M) [stretch]

**День 6 — Сб 25.07 · СИМУЛЯЦИЯ #1 · 5 задач за раз (~2.5 ч)**
Режим контеста: 5 смешанных задач по паттернам 1–5, без подсказок, засекаешь время.
Потом разбор со мной: что затормозило, какие паттерны просели.

**День 7 — Вс 26.07 · Разгрузка · ~4 задачи (1–1.5 ч)**
Добираем 2 самых слабых паттерна недели. Остальное — отдых/велик.

### Неделя 2

**День 8 — Пн 27.07 · Fast & Slow Pointers + связные списки · 6 задач**
Python: класс `ListNode`, dummy-узел.
1. Reverse Linked List (E)
2. Middle of the Linked List (E)
3. Linked List Cycle (E)
4. Happy Number (E)
5. Remove Nth Node From End of List (M)
6. Palindrome Linked List (M)

**День 9 — Вт 28.07 · Деревья BFS/DFS · 7 задач**
Python: рекурсия, `deque` для BFS.
1. Maximum Depth of Binary Tree (E)
2. Invert Binary Tree (E)
3. Same Tree (E)
4. Diameter of Binary Tree (E)
5. Binary Tree Level Order Traversal (M)
6. Validate Binary Search Tree (M)
7. Lowest Common Ancestor of a BST (M)

**День 10 — Ср 29.07 · Графы BFS/DFS · 6 задач**
Python: список смежности, `visited`-множество, `deque`.
1. Flood Fill (E)
2. Number of Islands (M)
3. Rotting Oranges (M)
4. Clone Graph (M)
5. Course Schedule (M) — топосортировка
6. Pacific Atlantic Water Flow (M) [stretch]

**День 11 — Чт 30.07 · Heap / Top-K · 5 задач**
Python: `heapq`, кортежи в куче.
1. Last Stone Weight (E)
2. Kth Largest Element in an Array (M)
3. Top K Frequent Elements — теперь через кучу (M)
4. K Closest Points to Origin (M)
5. Merge k Sorted Lists (H) [stretch]

**День 12 — Пт 31.07 · Prefix Sums / Intervals · 6 задач**
Python: массив префиксов, сортировка интервалов.
1. Running Sum of 1d Array (E)
2. Find Pivot Index (E)
3. Subarray Sum Equals K (M) — префиксы + хеш
4. Merge Intervals (M)
5. Insert Interval (M)
6. Non-overlapping Intervals (M)

**День 13 — Сб 01.08 · СИМУЛЯЦИЯ #2 · полный контест (до 5 ч)**
Боевые условия: 5 задач, до 5 часов, как реальный стажёрский контест. Разбор.

**День 14 — Вс 02.08 · Разгрузка · ~4 задачи**
Добор слабого. Отдых.

### Неделя 3 (добиваем 2 паттерна + переход к собесам)

**День 15 — Пн 03.08 · Backtracking · 6 задач**
Python: рекурсия «выбрал → откатил».
1. Subsets (M)
2. Combination Sum (M)
3. Permutations (M)
4. Generate Parentheses (M)
5. Letter Combinations of a Phone Number (M)
6. Word Search (M)

**День 16 — Вт 04.08 · Динамика (база) · 6 задач**
Python: мемоизация (`dict`) и табуляция.
1. Climbing Stairs (E)
2. Min Cost Climbing Stairs (E)
3. House Robber (M)
4. Coin Change (M)
5. Longest Increasing Subsequence (M)
6. Unique Paths (M)

> ✅ К 4 августа: все 11 паттернов закрыты, ~90 задач решено. Ты **готов к контесту**.

---

## Фаза 2 — Собеседования (5 августа → начало сентября)

**Ср 05.08 — открываешь реальные контесты** (Т-Банк / МТС), проходишь **сам**. Дальше — режим собесов.

Дневной шаблон (будни, ~2.5–3 ч):
- 1 **mock-собес** со мной: 2 задачи в «блокноте» без запуска (как в Яндексе), я интервьюер.
- 2–3 **medium** на самые слабые паттерны.
- Раз в неделю (Сб) — симуляция/полный mock; Вс — разгрузка.

Добираем продвинутые подтемы по мере надобности: Дейкстра, Union-Find, Trie, 2D-динамика,
сложные интервалы. Параллельно — живые секции компаний (даты выбираешь сам) и заявка в Сбер.

**Цель к началу сентября:** medium за 30–35 мин стабильно, ~130–150 задач суммарно,
старт стажировки → справка для МИЭТ.

---

## Сводка по объёму

| Блок | Задач |
|---|---|
| 12 паттерн-дней × ~6 | ~72 |
| 2 симуляции × 5 | ~10 |
| 2 разгрузки × ~4 | ~8 |
| **Итого к 4 августа** | **~90** |
| Фаза 2 (август, mock + medium) | +50–60 |
| **Итого к сентябрю** | **~140–150** |
