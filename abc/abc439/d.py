from bisect import bisect_left, bisect_right
from collections import defaultdict


def solve(N, A):
    X7 = defaultdict(list)
    X3 = defaultdict(list)
    for i, a in enumerate(A):
        x = a * 5 // 7
        if 7 * x == 5 * a:
            X7[x].append(i)

        x = a * 5 // 3
        if 3 * x == 5 * a:
            X3[x].append(i)

    ans = 0
    for j, a in enumerate(A):
        m = bisect_left(X7[a], j)
        n = bisect_left(X3[a], j)
        ans += m * n

        m = len(X7[a]) - bisect_right(X7[a], j)
        n = len(X3[a]) - bisect_right(X3[a], j)
        ans += m * n

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
