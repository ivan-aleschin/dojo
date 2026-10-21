"""Контракт структуры: на эти пути ссылаются заметки в Obsidian.

Obsidian ссылается на папку паттерна в main:
https://git.aleschin.ru/ivan-aleschin/dojo/src/branch/main/algorithms/<паттерн>
Поэтому папки паттернов и уроки нельзя переименовывать и удалять — только добавлять.
Новый паттерн → добавить строку в PATTERNS.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

# папка в algorithms/ → урок в docs/patterns/
PATTERNS = {
    "hash_map": "01-hash-map.md",
    "two_pointers": "02-two-pointers.md",
    "sliding_window": "03-sliding-window.md",
    "binary_search": "04-binary-search.md",
    "stack": "05-stack.md",
    "prefix_sums": "06-prefix-sums.md",
    "fast_slow": "07-fast-slow.md",
    "trees": "08-trees.md",
    "graphs": "09-graphs.md",
    "heap_topk": "10-heap-topk.md",
    "backtracking_dp": "11-backtracking-dp.md",
}

TASK_DIR = re.compile(r"^\d{2}_[a-z0-9_]+$")


@pytest.mark.parametrize("pattern", PATTERNS)
def test_pattern_folder_has_readme(pattern: str) -> None:
    assert (ROOT / "algorithms" / pattern / "README.md").is_file()


@pytest.mark.parametrize(("pattern", "lesson"), PATTERNS.items())
def test_readme_links_existing_lesson(pattern: str, lesson: str) -> None:
    assert (ROOT / "docs" / "patterns" / lesson).is_file()
    readme = (ROOT / "algorithms" / pattern / "README.md").read_text()
    assert f"docs/patterns/{lesson}" in readme


def test_no_unknown_pattern_folders() -> None:
    folders = {p.name for p in (ROOT / "algorithms").iterdir() if p.is_dir()}
    assert folders - {"__pycache__"} == set(PATTERNS)


@pytest.mark.parametrize("pattern", PATTERNS)
def test_task_folders_follow_convention(pattern: str) -> None:
    for task in (ROOT / "algorithms" / pattern).iterdir():
        if not task.is_dir() or task.name == "__pycache__":
            continue
        assert TASK_DIR.match(task.name), task
        assert (task / "solution.py").is_file(), task
