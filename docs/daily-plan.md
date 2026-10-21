# daily-plan — подготовка по неделям (старт 22 октября 2026, Чт)

Стратегия, компании и режим дня — в [`prep-plan.md`](prep-plan.md).
Годовой фундамент — в [`growth-plan.md`](growth-plan.md).
Материалы: [`python/`](python/01-basics-types.md), [`patterns/`](patterns/01-hash-map.md).

`(E)` = easy, `(M)` = medium, `[stretch]` = если осталось время.

**Неделя:** пн/вт/пт/чт вечер — 2–3 задачи (~1.5–2 ч), **ср — 4–5 задач (3–4 ч)**,
вс — 3–4 задачи или симуляция/mock, **сб — отдых** (пары).
Учебные блоки по 30–45 мин между проверками агентов.

Каждая задача: уточнения → идея и `O()` вслух → код → доктест → разбор со мной.

---

## Неделя 0 — 21–25.10 · старт

**Ср 21.10 — организационное (~1 ч)**
- [ ] `resume.md` обновлён: almanako, iskra, инфраструктура, работа с агентами
- [ ] Проверены открытые волны: Т-Банк, Авито, МТС, WB, Сбер, Ozon Camp (даты → `prep-plan.md` §3)
- [ ] Предупредить кафедру: смена места практики — вероятно в феврале

**Чт 22.10 · `python/` 01–02** — набирать руками, мини-задачи в `python_drills/`
**Пт 23.10 · `python/` 03–04** — enumerate/zip/sorted(key=), Counter/deque/heapq/bisect
**Вс 25.10 · `python/` 05–08 + разминка**
- 05 классы/ListNode/TreeNode, 06 stdin и контестный шаблон, 07 грабли (самотест!), 08 O(...)
- Разминка на скорость (по 10 мин): Two Sum (E), Contains Duplicate (E), Valid Anagram (E)
- [ ] Самотест модуля 07 без ошибок
- [ ] Контестный шаблон набран руками (сверить с `templates/contest_solution.py`)

---

## Неделя 1 — 26.10–01.11 · Hash Map, Two Pointers, Sliding Window, Binary Search

- **Пн 26.10 · Hash Map** → `patterns/01-hash-map.md`: Single Number (E), Intersection of Two Arrays (E)
- **Вт 27.10 · Hash Map:** Group Anagrams (M), Isomorphic Strings (M), Longest Consecutive Sequence (M)
- **Ср 28.10 · Two Pointers** → `patterns/02-two-pointers.md`:
  Valid Palindrome (E, *стаб уже в репо*), Remove Duplicates (E), Squares of a Sorted Array (E),
  Merge Sorted Array (E), Container With Most Water (M), [stretch] 3Sum (M)
- **Чт 29.10 · Sliding Window** → `patterns/03-sliding-window.md`:
  Maximum Average Subarray I (E), Best Time to Buy and Sell Stock (E)
- **Пт 30.10 · Sliding Window:** Longest Substring Without Repeating (M),
  Minimum Size Subarray Sum (M), Longest Repeating Character Replacement (M)
- **Вс 01.11 · Binary Search** → `patterns/04-binary-search.md`:
  Binary Search (E, без `bisect`), Search Insert Position (E), First and Last Position (M),
  Search in Rotated Sorted Array (M), Koko Eating Bananas (M) — бинпоиск по ответу

Фон: *Грокаем алгоритмы* — главы под паттерны недели.

---

## Неделя 2 — 02–08.11 · Stack, Prefix Sums, симуляция #1

- [ ] **Пн 02.11 — подать заявку в Т-Банк.** Экзамен ≈ через 2 недели; дату вписать сюда: `______`
- **Пн 02.11 · Stack** → `patterns/05-stack.md`: Valid Parentheses (E), Next Greater Element I (E)
- **Вт 03.11 · Stack:** Min Stack (M), Evaluate RPN (M), Daily Temperatures (M)
- **Ср 04.11 · Prefix Sums / Intervals** → `patterns/06-prefix-sums.md`:
  Running Sum (E), Find Pivot Index (E), Product of Array Except Self (M),
  Subarray Sum Equals K (M), Merge Intervals (M)
- **Чт 05.11 – Пт 06.11 · добор** — 2–3 задачи по самому слабому из паттернов 1–6
- **Вс 08.11 · СИМУЛЯЦИЯ #1** — 5 смешанных задач по паттернам 1–6, таймер, stdin
  (`templates/contest_solution.py`). Разбор: что затормозило.

> ✅ 6 паттернов отбора закрыты, ~35 задач.

---

## Неделя 3 — 09–15.11 · Списки и деревья

- **Пн 09.11 · Добор** по итогам симуляции #1 (2–3 задачи)
- **Вт 10.11 · Fast & Slow** → `patterns/07-fast-slow.md`: Reverse Linked List (E), Linked List Cycle (E)
- **Ср 11.11 · Списки + деревья:** Remove Nth Node From End (M), Palindrome Linked List (M);
  → `patterns/08-trees.md`: Maximum Depth (E), Invert Binary Tree (E)
- **Чт 12.11 · Деревья:** Level Order Traversal (M), Validate BST (M)
- **Пт 13.11 · Деревья:** Lowest Common Ancestor (M), Diameter of Binary Tree (E)
- **Вс 15.11 · Повторение 1–6 перед экзаменом Т-Банка:** 4 задачи на время, по одной из разных паттернов

---

## Неделя 4 — 16–22.11 · Графы и куча

- [ ] **Подать: Wildberries, Сбер, МТС** (тест приходит через несколько дней — к этому моменту готовы)
- [ ] **Авито** — если волна открыта, подать
- [ ] **Экзамен Т-Банка** (дата из ЛК)
- **Пн–Вт · Графы** → `patterns/09-graphs.md`: Flood Fill (E), Number of Islands (M), Rotting Oranges (M)
- **Ср 18.11 · Графы:** Course Schedule (M), Clone Graph (M), 01 Matrix (M), Pacific Atlantic (M)
- **Чт–Пт · Heap/Top-K** → `patterns/10-heap-topk.md`: Last Stone Weight (E), Kth Largest (M)
- **Вс 22.11 · Heap:** Top K Frequent (M), K Closest Points (M), Find Median from Data Stream (H, [stretch])

---

## Неделя 5 — 23–29.11 · Backtracking + DP (часть 1), симуляция #2

→ `patterns/11-backtracking-dp.md`
- **Пн–Вт · Backtracking:** Subsets, Permutations, Combination Sum
- **Ср 25.11:** Generate Parentheses, Letter Combinations, Word Search, Subsets II (дубликаты)
- **Чт–Пт · DP база:** Climbing Stairs, House Robber, Min Cost Climbing Stairs
- **Вс 29.11 · СИМУЛЯЦИЯ #2** — 5 задач по всем паттернам, таймер, stdin

---

## Неделя 6 — 30.11–06.12 · DP (часть 2) + Яндекс

- [ ] **Пн 30.11 — анкета в Яндекс.** Тест — в течение недели после анкеты, сдать до 06.12
- **Пн–Вт · DP:** House Robber II, Coin Change, Unique Paths
- **Ср 02.12:** Minimum Path Sum, LIS (оба решения), Word Break
- **Чт–Пт · тест Яндекса**
- **Вс 06.12:** Partition Equal Subset Sum, LCS
- [ ] Рассказ про almanako/iskra на 10 минут готов (`prep-plan.md` §8)

---

## Неделя 7 — 07–13.12 · Продвинутое + mock №1

- [ ] **Ozon Camp — подать** (проверить дедлайн IT-трека)
- **Пн–Вт:** Дейкстра (Network Delay Time), Union-Find (Number of Provinces)
- **Ср 09.12:** Trie (Implement Trie), LRU Cache, Edit Distance
- **Чт–Пт:** SQL под секции — JOIN, GROUP BY, оконные функции (`backend-roadmap.md` §2, pgexercises)
- **Вс 13.12 · MOCK №1** — 2 задачи в блокноте без запуска (`prep-plan.md` §6)

---

## Неделя 8 — 14–20.12 · Секции: бэкенд + mock №2

- **Пн–Пт вечера:** бэкенд-темы под секции — HTTP и статус-коды, транзакции и уровни изоляции,
  индексы и N+1, async/GIL (`backend-roadmap.md` §1, 2, 8)
- **Ср 16.12:** 3 задачи medium на время + разбор слабых паттернов
- **Вс 20.12 · MOCK №2** — алгоритмы + 15 мин вопросов «про проект»

> ✅ К 20.12: 11 паттернов, ~110 задач, 2 симуляции, 2 mock. Готов к секциям.

---

## 21.12–31.01 · Сессия + секции и финалы

Новых тем нет. Нагрузка падает из-за сессии — держим форму, а не набираем.

**Каждую неделю:**
- 1 mock (воскресенье): 2 задачи без запуска, 60–70 мин
- 2–3 задачи medium по самому слабому паттерну
- повторение чек-листа одного паттерна в день — вслух, без кода (5 мин)
- понедельник: статусы заявок, новые волны

**После каждой реальной секции** — разбор в `journal/interviews/<компания>.md` в тот же день.

**31.01.2027 — КОНТРОЛЬНАЯ ТОЧКА.**
- Есть оффер → выход, бумага о смене места практики, `prep-plan.md` §7 (как пройти стажировку).
- Нет оффера → **план B**: февраль–март — фундамент (`growth-plan.md`, треки 3–4) +
  1 mock в неделю; весенние наборы на лето (март–апрель); старт июнь–июль после выпуска.

---

## Сводка по объёму

| Период | Задач |
|---|---|
| Python-разминка (25.10) | 3 |
| Паттерны 1–6 + симуляция #1 (26.10–08.11) | ~35 |
| Списки, деревья, графы, куча (09–22.11) | ~30 |
| Backtracking + DP + симуляция #2 (23.11–06.12) | ~25 |
| Продвинутое + mock (07–20.12) | ~15 |
| **Итого к 20.12** | **~110** |
| Сессия, секции (до 31.01) | +15–20 |
