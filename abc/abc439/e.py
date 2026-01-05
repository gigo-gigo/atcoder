from bisect import bisect_left


def calc_longest_increasing_subsequence(A: list[int]) -> int:
    """Longest Increasing Subsequence (LIS) problem.

    Args:
        A (List): Array.

    Returns:
        int: LIS value.
    """
    X: list[int] = []
    for a in A:
        i = bisect_left(X, a)
        if i < len(X):
            X[i] = a
        else:
            X.append(a)

    return len(X)


def solve(X, Y):
    XY = sorted((x, -y) for x, y in zip(X, Y))
    A = [-y for _, y in XY]
    ans = calc_longest_increasing_subsequence(A)

    return ans


def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = solve(X, Y)
    print(ans)


if __name__ == "__main__":
    main()
