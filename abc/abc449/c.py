from bisect import bisect_left, bisect_right
from collections import defaultdict


def solve(N, L, R, S):
    X = defaultdict(list)
    for i, s in enumerate(S):
        X[s].append(i)

    ans = 0
    for A in X.values():
        for i in A:
            m = bisect_right(A, i + R) - bisect_left(A, i + L)
            ans += m

    return ans


def main():
    N, L, R = list(map(int, input().split()))
    S = input()
    ans = solve(N, L, R, S)
    print(ans)


if __name__ == "__main__":
    main()
