# Coding Dojo — подготовка к стажировке (Backend Python)

Учебный репозиторий: алгоритмические паттерны, задачи, план подготовки и разбор компаний.
Цель — **оффер стажировки со стартом в январе–феврале 2027** (план B — лето 2027),
затем конверсия в штат на максимальный грейд.

---

## ▶️ Начни отсюда

1. **[`docs/DAILY_PLAN.md`](docs/DAILY_PLAN.md)** — что делать на этой неделе (старт 22.10.2026).
2. **[`docs/PREP_PLAN.md`](docs/PREP_PLAN.md)** — стратегия, компании, когда подавать.
3. **[`docs/GROWTH_PLAN.md`](docs/GROWTH_PLAN.md)** — годовой трек фундамента: книги, тренажёры.

Заявки подаём, когда готовы к их отбору: Т-Банк — 02.11, WB/Сбер/МТС — 16–22.11,
Яндекс — 30.11, Ozon — до конца декабря.

---

## Навигация

| Файл | Зачем |
|---|---|
| **[`docs/DAILY_PLAN.md`](docs/DAILY_PLAN.md)** | что делать на этой неделе — план до 31.01.2027 |
| **[`docs/PREP_PLAN.md`](docs/PREP_PLAN.md)** | стратегия, компании, дедлайны, режим дня, прогресс по паттернам |
| **[`docs/README.md`](docs/README.md)** | учебные материалы: Python, паттерны, шаблоны, компании |
| [`docs/companies/shortlist.md`](docs/companies/shortlist.md) | куда подаваться, когда и почему |
| **[`docs/GROWTH_PLAN.md`](docs/GROWTH_PLAN.md)** | годовой фундамент: Linux, сети, БД, DDIA, инфраструктура |
| [`docs/RESUME.md`](docs/RESUME.md) | резюме |
| [`docs/BACKEND_ROADMAP.md`](docs/BACKEND_ROADMAP.md) | бэкенд-темы на поздние секции (SQL, FastAPI, дизайн) |
| [`CLAUDE.md`](CLAUDE.md) | протокол работы с ИИ-тренером |

## Структура

```
dojo/
├── CLAUDE.md               # протокол работы с ИИ-тренером
├── docs/                   # ВСЁ остальное: планы, курсы, шаблоны, компании
│   ├── DAILY_PLAN.md       # план по неделям
│   ├── PREP_PLAN.md        # стратегия, компании, дедлайны, прогресс
│   ├── GROWTH_PLAN.md      # годовой трек фундамента
│   ├── RESUME.md
│   ├── BACKEND_ROADMAP.md
│   ├── python/             # 8 модулей экспресс-повторения Python (2 дня)
│   ├── patterns/           # 11 уроков по паттернам: теория, эталон, задачи, чек-лист
│   ├── templates/          # заготовки: задача, эталон, стаб, контест, конспект, mock
│   └── companies/          # куда подаваться + разбор списка ОРИОКС
│
├── algorithms/             # РЕШЕНИЯ ПО ПАТТЕРНАМ — 11 папок, в каждой чек-лист задач
│   └── <паттерн>/<NN_имя>/solution.py
│
├── python_drills/          # ТРЕНИРОВКА ПО PYTHON — файл на каждый модуль docs/python
│   └── <NN_модуль>.py
│
├── notes/                  # КОНСПЕКТЫ: день, mock-собес, разборы реальных секций
│   └── interviews/
│
├── coderun/                # задачи с coderun.yandex.ru
│   └── <NNNN_имя>/{README.md, solution.py}
│
├── pyproject.toml          # pytest настроен на --doctest-modules
├── flake.nix               # dev-окружение (Nix)
└── uv.lock
```

## Куда что писать

| Что | Куда | Заготовка |
|---|---|---|
| мини-задачи из модулей Python | [`python_drills/<NN_модуль>.py`](python_drills/README.md) | файлы уже заведены, задачи в шапке |
| задачи по паттерну | [`algorithms/<паттерн>/<NN_имя>/solution.py`](algorithms/hash_map/README.md) | [`docs/templates/solution_stub.py`](docs/templates/solution_stub.py) |
| задача с контеста | `coderun/<NNNN_имя>/` | [`docs/templates/coderun_task.md`](docs/templates/coderun_task.md) |
| конспект дня | [`notes/YYYY-MM-DD_<паттерн>.md`](notes/README.md) | [`docs/templates/day_notes.md`](docs/templates/day_notes.md) |
| mock-собес | `notes/YYYY-MM-DD_mock.md` | [`docs/templates/mock_interview.md`](docs/templates/mock_interview.md) |
| разбор реальной секции | `notes/interviews/<компания>.md` | — |

## Как устроена работа над задачей

1. **Уточняющие вопросы** — диапазоны, дубликаты, пустой ввод, отсортирован ли.
2. **Идея и сложность вслух** — до кода, всегда.
3. **Код** — в `solution.py`, доктесты делаем зелёными.
4. **Разбор** — edge-кейсы, `O(время)/O(память)`, что можно улучшить.

Полный протокол и роль тренера — в [`CLAUDE.md`](CLAUDE.md), протокол mock-собеса —
в [`docs/PREP_PLAN.md`](docs/PREP_PLAN.md) §6.

## Конвенции

- Одна задача = одна папка с `solution.py`.
- Примеры оформляются **доктестами** в docstring — они же и есть тесты.
- Эталон = рабочее решение. Задача = стаб с доктестами и `raise NotImplementedError`.
- Python 3.14, современный синтаксис (`list[int]`, `int | None`), ruff + mypy strict.

## Запуск

```bash
pytest                                        # весь репозиторий
python -m doctest <путь>/solution.py -v       # одна задача
```

> Красный тест `02_valid_palindrome` — это нормально: нерешённая задача.
> Она станет зелёной, когда ты её решишь.
