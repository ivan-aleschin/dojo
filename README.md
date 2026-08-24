# Coding Dojo — подготовка к стажировке (Backend Python)

Учебный репозиторий: алгоритмические паттерны, задачи, план подготовки.

## С чего начать

| Файл | Зачем |
|---|---|
| **[`PREP_PLAN.md`](PREP_PLAN.md)** | стратегия, компании, дедлайны, прогресс по паттернам |
| **[`DAILY_PLAN.md`](DAILY_PLAN.md)** | что делать сегодня — план по дням |
| **[`docs/README.md`](docs/README.md)** | учебные материалы: Python и 11 паттернов |
| [`RESUME.md`](RESUME.md) | резюме |
| [`BACKEND_ROADMAP.md`](BACKEND_ROADMAP.md) | бэкенд-темы на потом (SQL, FastAPI, безопасность) |
| [`CLAUDE.md`](CLAUDE.md) | протокол работы с ИИ-тренером |

## Структура

```
dojo/
├── docs/
│   ├── python/             # 8 модулей экспресс-повторения Python
│   ├── patterns/           # 11 уроков по паттернам: теория, эталон, задачи, чек-лист
│   └── template_coderun.md # шаблон описания задачи с CodeRun
│
├── algorithms/             # решения по паттернам
│   └── <паттерн>/<NN_имя>/solution.py
│
├── coderun/                # задачи с coderun.yandex.ru
│   └── <NNNN_имя>/{README.md, solution.py}
│
├── pyproject.toml          # pytest настроен на --doctest-modules
├── flake.nix               # dev-окружение (Nix)
└── uv.lock
```

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
