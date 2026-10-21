# docs/templates — заготовки

Копируешь, переименовываешь, заполняешь. Ничего не выдумываешь каждый раз заново.

| Шаблон | Куда кладётся | Когда |
|---|---|---|
| [`coderun-task.md`](coderun-task.md) | `coderun/<NNNN_имя>/README.md` | задача с контеста: условие + разбор после решения |
| [`leetcode-task.md`](leetcode-task.md) | `algorithms/<паттерн>/<NN_имя>/README.md` | задача по паттерну, если условие требует пояснений |
| [`solution_stub.py`](solution_stub.py) | `<...>/<NN_имя>/solution.py` | **задача Ивану**: доктесты есть, тело — `NotImplementedError` |
| [`solution_reference.py`](solution_reference.py) | `<...>/<NN_имя>/solution.py` | **эталон**: рабочее решение + почему оно корректно |
| [`contest_solution.py`](contest_solution.py) | черновик на время контеста | формат stdin→stdout отборочных экзаменов |
| [`day-notes.md`](day-notes.md) | рядом с задачами дня или в заметках | мини-конспект в конце учебного дня, 5 минут |
| [`mock-interview.md`](mock-interview.md) | заметки | бланк тренировочной секции (протокол — `../prep-plan.md` §6) |

Соглашения репозитория (имена папок, доктесты, запуск) — в
[корневом README](../../README.md) и `CLAUDE.md`.

> ⚠️ `.py`-шаблоны лежат в `docs/`, а не в `algorithms/`, поэтому pytest их не собирает
> (`testpaths` в `pyproject.toml`). Доктест в `solution_stub.py` намеренно падает —
> это и есть его смысл.
