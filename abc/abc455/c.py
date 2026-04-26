from collections import Counter


def solve(N, K, A):
    cnt = Counter(A)
    X = sorted(k * v for k, v in cnt.items())
    ans = sum(A) - sum(X[-K:])

    return ans


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, K, A)
    print(ans)


if __name__ == "__main__":
    main()
