# Coding Dojo: алгоритмы, LeetCode, CodeRun, FastAPI

## Структура

```
dojo/
├── pyproject.toml
├── README.md
├── .python-version         # uv читает этот файл для выбора интерпретатора
├── uv.lock
├── flake.nix
├── flake.lock
├── conftest.py             # глобальные фикстуры pytest (если нужны)
│
├── algorithms/             # чистые алгоритмы, без привязки к платформе
│   ├── sorting/
│   │   ├── merge_sort/
│   │   │   ├── solution.py
│   │   │   └── test_solution.py
│   │   └── quick_sort/
│   │       ├── solution.py
│   │       └── test_solution.py
│   ├── searching/
│   │   └── binary_search/
│   │       ├── solution.py  # содержит docstring с примерами → doctest
│   │       └── test_solution.py
│   ├── graphs/
│   ├── dp/                 # dynamic programming
│   └── data_structures/
│
├── leetcode/
│   ├── easy/
│   │   └── 0001_two_sum/
│   │       ├── solution.py
│   │       └── test_solution.py
│   ├── medium/
│   │   └── 0033_search_in_rotated_array/
│   │       ├── solution.py
│   │       └── test_solution.py
│   └── hard/
│
├── coderun/                # coderun.yandex.ru
│   └── 0042_problem_name/
│       ├── solution.py
│       └── test_solution.py
│
├── fastapi_practice/       # отдельно, потому что это веб, а не алго
│   ├── 01_basics/
│   │   ├── app.py
│   │   └── test_app.py     # через httpx + pytest-asyncio
│   └── 02_todo_api/
│
└── playground/             # черновики, эксперименты без тестов
```
