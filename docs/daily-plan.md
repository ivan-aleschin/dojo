# daily-plan — подготовка по неделям (старт 22 октября 2026, Чт)

Стратегия, компании и режим дня — в [`prep-plan.md`](prep-plan.md).
Годовой фундамент — в [`growth-plan.md`](growth-plan.md).
Материалы: [`python/`](python/01-basics-types.md), [`patterns/`](patterns/01-hash-map.md).

`(E)` = easy, `(M)` = medium, `[stretch]` = если осталось время.
Каждая задача: уточнения → идея и `O()` вслух → код → доктест → разбор со мной.

---

## Неделя-шаблон

Расписание снято из kalendaro и tutorejo 21.10.2026 (сентябрь–декабрь). Учёба в МИЭТ —
только лабы и практики, недели чередуются: **A** — 26.10, 09.11, 23.11, 07.12, 21.12;
**B** — 02.11, 16.11, 30.11, 14.12.

| День | Занято | Учёба в dojo |
|---|---|---|
| **Пн** | «Практика» МИЭТ = своя работа над ВКР (iskra) через агентов; уроки 17–21 | **главный блок 10–16: 4 задачи** (~3.5 ч), ВКР — агенты в фоне |
| **Вт** | уроки 19–21 | **длинный блок 10–18: 3 задачи + 1 ч фундамента**; симуляции и mock — здесь |
| **Ср** | уроки 16–18; лаба 18:30 (A, пока не закрыта) | **блок 10–15: 4 задачи** (~3 ч) |
| **Чт** | МИЭТ с 14:00–15:30 до ~20; урок 20–21 | утро: 2 задачи или повторение (~1.5 ч) |
| **Пт** | философия (A 9:00 / B 12:00); уроки 16–22 | без задач; 30–60 мин книги, если есть силы |
| **Сб** | метрология 12:00 (A); урок 14–15 | отдых; по желанию — книга |
| **Вс** | — | **отдых, обязательно** |

Итого ~13 задач и ~12 ч в неделю.

**Бюджет недели (оценка):**

| На что | Часов |
|---|---|
| Репетиторство | 15–17 (+2–4, если добавятся ученики) |
| dojo: алгоритмы + книги | ~12 |
| МИЭТ: лабы, практики, научрук + дорога | ~6–8 |
| ВКР (iskra) и almanako — постановка задач агентам и проверки | ~5 |
| Зал (3–4 раза) + английский | ~7–8 |
| **Итого** | **~45–50**, воскресенье свободно целиком |

almanako и ВКР — в фоне: задачи агентам перед блоком,
проверка 15 минут по таймеру между задачами. Научрук (раз в 2 недели) и новые ученики —
ставить на пт/сб или после 18:00, **не в блоки пн–ср**.

---

## Неделя 0 — 21–25.10 · старт

- [ ] **Ср 21.10:** `resume.md` обновлён (almanako, iskra, инфраструктура, работа с агентами);
      подписка на @tbank_education (новые волны Т-Банка); заявок до декабря нет (→ `prep-plan.md` §3)
- [ ] Предупредить кафедру: смена места практики — вероятно в феврале
- **Чт 22.10 утро · `python/` 01–02** — набирать руками, упражнения в `python/`
- **Пт 23.10 утро · `python/` 03–04** — enumerate/zip/sorted(key=), Counter/deque/heapq/bisect
- **Сб 24.10 до 14:00 · `python/` 05–06** — классы, ListNode/TreeNode, stdin и шаблон контеста

---

## Неделя 1 — 26.10–01.11 (A) · Python + Hash Map + Two Pointers

- **Пн 26.10 · `python/` 07–08 + разминка**: грабли (самотест!), O(...);
  Two Sum (E), Contains Duplicate (E), Valid Anagram (E) — по 10 мин
- **Вт 27.10 · Hash Map** → `patterns/01-hash-map.md`: Single Number (E),
  Intersection of Two Arrays (E), Group Anagrams (M), Isomorphic Strings (M),
  Longest Consecutive Sequence (M)
- **Ср 28.10 · Two Pointers** → `patterns/02-two-pointers.md`: Valid Palindrome (E, *стаб уже в репо*),
  Remove Duplicates (E), Squares of a Sorted Array (E), Container With Most Water (M), [stretch] 3Sum (M)
- **Чт 29.10 утро · Sliding Window** → `patterns/03-sliding-window.md`:
  Maximum Average Subarray I (E), Best Time to Buy and Sell Stock (E)

Фон: «Грокаем алгоритмы» — главы под темы недели.

---

## Неделя 2 — 02–08.11 (B) · Sliding Window, Binary Search, Stack

- **Пн 02.11 · Sliding Window:** Longest Substring Without Repeating (M),
  Minimum Size Subarray Sum (M), Longest Repeating Character Replacement (M), Merge Sorted Array (E)
- **Вт 03.11 · Binary Search** → `patterns/04-binary-search.md`: Binary Search (E, без `bisect`),
  Search Insert Position (E), First and Last Position (M) + 1 ч фундамента
- **Ср 04.11 · Binary Search + Stack:** Search in Rotated Sorted Array (M), Koko Eating Bananas (M);
  → `patterns/05-stack.md`: Valid Parentheses (E), Min Stack (M)
- **Чт 05.11 утро · Stack:** Daily Temperatures (M), Evaluate RPN (M)

---

## Неделя 3 — 09–15.11 (A) · Prefix Sums + симуляция #1

- **Пн 09.11 · Prefix Sums / Intervals** → `patterns/06-prefix-sums.md`: Running Sum (E),
  Find Pivot Index (E), Product of Array Except Self (M), Subarray Sum Equals K (M)
- **Вт 10.11 · СИМУЛЯЦИЯ #1** — 5 задач по паттернам 1–6, таймер, stdin
  (`templates/contest_solution.py`). Разбор → `journal/simulations/2026-11-10.md`
- **Ср 11.11 · Добор** по итогам симуляции (2 задачи) + Merge Intervals (M), Next Greater Element I (E)
- **Чт 12.11 утро · Fast & Slow** → `patterns/07-fast-slow.md`: Reverse Linked List (E), Linked List Cycle (E)

> ✅ 6 паттернов отбора закрыты, ~40 задач.

---

## Неделя 4 — 16–22.11 (B) · Списки, деревья, графы

- **Пн 16.11 · Списки + деревья:** Remove Nth Node From End (M), Palindrome Linked List (M);
  → `patterns/08-trees.md`: Maximum Depth (E), Invert Binary Tree (E)
- **Вт 17.11 · Деревья:** Level Order Traversal (M), Validate BST (M), Lowest Common Ancestor (M)
  + 1 ч фундамента
- **Ср 18.11 · Графы** → `patterns/09-graphs.md`: Flood Fill (E), Number of Islands (M),
  Rotting Oranges (M), Course Schedule (M)
- **Чт 19.11 утро · Повторение 1–6:** 2 задачи на время

---

## Неделя 5 — 23–29.11 (A) · Графы, куча, backtracking

- **Пн 23.11 · Графы + Heap:** Clone Graph (M), 01 Matrix (M);
  → `patterns/10-heap-topk.md`: Last Stone Weight (E), Kth Largest (M)
- **Вт 24.11 · Heap + Backtracking:** Top K Frequent (M), K Closest Points (M);
  → `patterns/11-backtracking-dp.md`: Subsets (M) + 1 ч фундамента
- **Ср 25.11 · Backtracking:** Permutations, Combination Sum, Generate Parentheses, Word Search
- **Чт 26.11 утро · DP база:** Climbing Stairs (E), Min Cost Climbing Stairs (E)

---

## Неделя 6 — 30.11–06.12 (B) · DP + симуляция #2

- **Пн 30.11 · DP:** House Robber, House Robber II, Coin Change, Unique Paths
- **Вт 01.12 · СИМУЛЯЦИЯ #2** — 5 задач по всем паттернам, таймер, stdin
- **Ср 02.12 · DP:** LIS (оба решения), Word Break, Minimum Path Sum, Subsets II (дубликаты)
- **Чт 03.12** — с 14:00 БЖД, задач нет
- [ ] Рассказ про almanako/iskra на 10 минут готов (`prep-plan.md` §8)

---

## Неделя 7 — 07–13.12 (A) · Продвинутое + mock №1

- [ ] **Ozon Camp — подать** (проверить дедлайн IT-направления)
- **Пн 07.12:** Network Delay Time (Дейкстра), Number of Provinces (Union-Find),
  Implement Trie, LRU Cache
- **Вт 08.12 · MOCK №1** — 2 задачи в блокноте без запуска (`prep-plan.md` §6)
  → `journal/mock/2026-12-08.md`; + 1 ч SQL (`backend-roadmap.md` §2, pgexercises)
- **Ср 09.12 · DP-добор:** LCS, Edit Distance, Partition Equal Subset Sum
- **Чт 10.12 утро:** SQL — JOIN, GROUP BY, оконные функции

---

## Неделя 8 — 14–20.12 (B) · Темы бэкенда для собесов + mock №2 + Яндекс

- [ ] **Пн 14.12 — анкета в Яндекс.** Тест — в течение недели: **Сб 19.12 утром** (свободная суббота)
      или Ср 16.12 вместо задач

- **Пн 14.12:** HTTP и коды ответа, транзакции и уровни изоляции, индексы и N+1
  (`backend-roadmap.md` §2, 8) + 2 задачи (M) на время
- **Вт 15.12 · MOCK №2** — алгоритмы + 15 мин вопросов про проект
- **Ср 16.12:** async/GIL (`backend-roadmap.md` §1) + 3 задачи (M) по слабым паттернам
- **Чт 17.12 утро:** повторение чек-листов паттернов вслух

> ✅ К 20.12: 11 паттернов, ~110 задач, 2 симуляции, 2 mock. Готов к собесам.

---

## 21.12–31.01 · Сессия + собесы

Новых тем нет. Сессия съедает время — держим форму, а не набираем новое.

**Каждую неделю:**
- 1 mock (вторник): 2 задачи без запуска, 60–70 мин
- 2–3 задачи (M) по самому слабому паттерну (пн/ср)
- 5 минут в день: чек-лист одного паттерна вслух, без кода
- понедельник: статусы заявок, новые волны (Т-Банк, Сбер, МТС)

**ВКР:** черновик целиком — **к 31.01** (дневное время пн–ср теперь можно отдавать ей).

Собесы Яндекса и Ozon — если тест пройден. **После каждой реальной секции** — разбор
в `journal/interviews/<компания>.md` в тот же день.

## Февраль–март 2027 · Волны и собесы

- Подаёмся в первую же волну Т-Банка, весенний набор МТС, Сбер (если есть направление)
- Перед каждым экзаменом — симуляция во вторник
- Параллельно — фундамент (`growth-plan.md`, ранг 2)
- **ВКР:** февраль — чистовик, **жёсткий срок 28.02** (`prep-plan.md` §1)

**31.03.2027 — КОНТРОЛЬНАЯ ТОЧКА.**
- Есть оффер → выход, бумага о смене места практики, `prep-plan.md` §7 (как пройти стажировку).
- Нет оффера → **план B**: летние наборы (Авито, МТС, Т-Банк), старт июнь–июль после выпуска.

---

## Сводка по объёму

| Период | Задач |
|---|---|
| Python-разминка (26.10) | 3 |
| Паттерны 1–6 + симуляция #1 (27.10–12.11) | ~40 |
| Списки, деревья, графы, куча (16–24.11) | ~25 |
| Backtracking + DP + симуляция #2 (24.11–02.12) | ~20 |
| Продвинутое + mock (07–17.12) | ~20 |
| **Итого к 20.12** | **~110** |
| Сессия, собесы, волны (янв–мар) | +30–40 |
