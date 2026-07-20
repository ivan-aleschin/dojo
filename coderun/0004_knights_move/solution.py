def count_knight_paths(n: int, m: int) -> int:
    """Количество маршрутов коня из левого верхнего угла (1,1) в правый нижний (n,m).

    Конь ходит только "вперёд": на 2 вниз + 1 вправо, либо на 1 вниз + 2 вправо.
    Поэтому клетки можно заполнять слева направо и сверху вниз обычной динамикой:
    dp[i][j] = число способов попасть в (i, j) = dp[i-2][j-1] + dp[i-1][j-2].

    >>> count_knight_paths(3, 2)
    1
    >>> count_knight_paths(31, 34)
    293930
    >>> count_knight_paths(1, 1)
    1
    """
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # путь нулевой длины тоже считается маршрутом
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            ways = 0
            if i - 2 >= 1 and j - 1 >= 1:
                ways += dp[i - 2][j - 1]
            if i - 1 >= 1 and j - 2 >= 1:
                ways += dp[i - 1][j - 2]
            dp[i][j] = ways
    return dp[n][m]


def main() -> None:
    n, m = map(int, input().split())
    print(count_knight_paths(n, m))


if __name__ == "__main__":
    main()
