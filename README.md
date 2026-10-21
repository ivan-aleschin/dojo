# Coding Dojo — подготовка к стажировке (Backend Python)

Учебный репозиторий: алгоритмические паттерны, задачи, план подготовки и разбор компаний.
Цель — **оффер стажировки со стартом зимой–весной 2027** (план B — лето 2027),
затем конверсия в штат на максимальный грейд.

---

## ▶️ Начни отсюда

1. **[`docs/daily-plan.md`](docs/daily-plan.md)** — что делать на этой неделе (старт 22.10.2026).
2. **[`docs/prep-plan.md`](docs/prep-plan.md)** — стратегия, компании, когда подавать.
3. **[`docs/growth-plan.md`](docs/growth-plan.md)** — годовой трек фундамента: книги, тренажёры.

До декабря — подготовка без заявок. Отборы — декабрь–март: Ozon Camp (до конца декабря),
Яндекс (14.12), следующие волны Т-Банка, Сбера и МТС (ожидаем февраль–март).

---

## Навигация

| Файл | Зачем |
|---|---|
| **[`docs/daily-plan.md`](docs/daily-plan.md)** | что делать на этой неделе — план до 31.03.2027 |
| **[`docs/prep-plan.md`](docs/prep-plan.md)** | стратегия, компании, дедлайны, режим дня, прогресс по паттернам |
| **[`docs/README.md`](docs/README.md)** | учебные материалы: Python, паттерны, шаблоны, компании |
| [`docs/companies/shortlist.md`](docs/companies/shortlist.md) | куда подаваться, когда и почему |
| **[`docs/growth-plan.md`](docs/growth-plan.md)** | годовой фундамент: Linux, сети, БД, DDIA, инфраструктура |
| [`docs/resume.md`](docs/resume.md) | резюме |
| [`docs/backend-roadmap.md`](docs/backend-roadmap.md) | бэкенд-темы на поздние секции (SQL, FastAPI, дизайн) |
| [`CLAUDE.md`](CLAUDE.md) | протокол работы с ИИ-тренером |

## Структура

```
dojo/
├── CLAUDE.md               # протокол работы с ИИ-тренером
├── docs/                   # ВСЁ остальное: планы, курсы, шаблоны, компании
│   ├── daily-plan.md       # план по неделям
│   ├── prep-plan.md        # стратегия, компании, дедлайны, прогресс
│   ├── growth-plan.md      # годовой трек фундамента
│   ├── resume.md
│   ├── backend-roadmap.md
│   ├── python/             # 8 модулей экспресс-повторения Python
│   ├── patterns/           # 11 уроков по паттернам: теория, эталон, задачи, чек-лист
│   ├── templates/          # заготовки: задача, эталон, стаб, контест, симуляция, mock
│   └── companies/          # куда подаваться + разбор списка ОРИОКС
│
├── algorithms/             # РЕШЕНИЯ ПО ПАТТЕРНАМ — 11 папок, в каждой чек-лист задач
│   └── <паттерн>/<NN_имя>/solution.py
│
├── python/                 # ТРЕНИРОВКА ПО PYTHON — файл на каждый модуль docs/python
│   └── <NN_модуль>.py
│
├── journal/                # ЖУРНАЛ ТРЕНИРОВОК (знания — в Obsidian)
│   └── mock/ simulations/ interviews/ internship/
│
├── tests/                  # контракт структуры для ссылок из Obsidian
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
| мини-задачи из модулей Python | [`python/<NN_модуль>.py`](python/README.md) | файлы уже заведены, задачи в шапке |
| задачи по паттерну | [`algorithms/<паттерн>/<NN_имя>/solution.py`](algorithms/hash_map/README.md) | [`docs/templates/solution_stub.py`](docs/templates/solution_stub.py) |
| задача с контеста | `coderun/<NNNN_имя>/` | [`docs/templates/coderun-task.md`](docs/templates/coderun-task.md) |
| конспект темы | Obsidian, своими словами | — |
| симуляция контеста | [`journal/simulations/YYYY-MM-DD.md`](journal/README.md) | [`docs/templates/simulation.md`](docs/templates/simulation.md) |
| mock-собес | `journal/mock/YYYY-MM-DD.md` | [`docs/templates/mock-interview.md`](docs/templates/mock-interview.md) |
| разбор реальной секции | `journal/interviews/<компания>.md` | — |

## Как устроена работа над задачей

1. **Уточняющие вопросы** — диапазоны, дубликаты, пустой ввод, отсортирован ли.
2. **Идея и сложность вслух** — до кода, всегда.
3. **Код** — в `solution.py`, доктесты делаем зелёными.
4. **Разбор** — edge-кейсы, `O(время)/O(память)`, что можно улучшить.

Полный протокол и роль тренера — в [`CLAUDE.md`](CLAUDE.md), протокол mock-собеса —
в [`docs/prep-plan.md`](docs/prep-plan.md) §6.

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
