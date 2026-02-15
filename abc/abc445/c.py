def solve(N, A):
    A = [0] + A
    X = [-1] * (N + 1)
    for u in range(N, 0, -1):
        X[u] = A[u] if u == A[u] else X[A[u]]

    return X[1:]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(*ans)


if __name__ == "__main__":
    main()
