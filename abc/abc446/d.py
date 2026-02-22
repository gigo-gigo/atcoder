from collections import Counter


def solve(N, A):
    X = Counter()
    for a in A[::-1]:
        X[a] = max(X[a], X[a + 1] + 1)

    ans = max(X.values())

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
