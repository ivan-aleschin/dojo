"""Шаблон КОНТЕСТНОГО решения: чтение stdin, вывод в stdout.

Формат отборочных экзаменов (Т-Банк, Яндекс.Контест, CodeRun) — именно такой,
а не «напиши функцию». Разбор — docs/python/06_io_contest.md.
"""

import bisect  # noqa: F401
import heapq  # noqa: F401
import sys
from collections import Counter, defaultdict, deque  # noqa: F401


def solve() -> None:
    data = sys.stdin.read().split()
    it = iter(data)

    n = int(next(it))
    nums = [int(next(it)) for _ in range(n)]

    # ── алгоритм ──────────────────────────────────────────────
    ans = sum(nums)

    print(ans)


if __name__ == "__main__":
    # sys.setrecursionlimit(300_000)   # раскомментировать при рекурсивном DFS
    solve()
