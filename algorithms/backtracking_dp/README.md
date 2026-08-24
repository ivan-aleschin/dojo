# Backtracking + DP — решения

Теория, разобранный эталон и типичные ошибки — в уроке
**[`docs/patterns/11_backtracking_dp.md`](../../docs/patterns/11_backtracking_dp.md)**.
Здесь только код: одна задача = одна папка `NN_имя/solution.py`.

## Прогресс

- [ ] 1. Subsets (M)
- [ ] 2. Combination Sum (M)
- [ ] 3. Permutations (M)
- [ ] 4. Generate Parentheses (M)
- [ ] 5. Letter Combinations of a Phone Number (M)
- [ ] 6. Word Search (M) — backtracking на сетке
- [ ] 7. Subsets II / Combination Sum II (M) — пропуск дубликатов
- [ ] 8. Palindrome Partitioning (M)
- [ ] 9. N-Queens (H) — классика, знать идею
- [ ] 10. Climbing Stairs (E)
- [ ] 11. Min Cost Climbing Stairs (E)
- [ ] 12. House Robber (M)
- [ ] 13. House Robber II (M)
- [ ] 14. Coin Change (M)
- [ ] 15. Longest Increasing Subsequence (M)
- [ ] 16. Unique Paths (M)
- [ ] 17. Minimum Path Sum (M)
- [ ] 18. Word Break (M)
- [ ] 19. Longest Common Subsequence (M)
- [ ] 20. Partition Equal Subset Sum (M)
- [ ] 21. Edit Distance (H)

## Как решать

1. Уточняющие вопросы к условию.
2. Идея и `O(время)` / `O(память)` — вслух, до кода.
3. Код, доктесты зелёные.
4. Разбор со мной: edge-кейсы, что можно улучшить.

```bash
python -m doctest algorithms/backtracking_dp/NN_имя/solution.py -v
pytest algorithms/backtracking_dp
```

Шаблоны решения — в [`docs/templates/`](../../docs/templates/README.md).
