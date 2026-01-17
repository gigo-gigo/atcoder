from itertools import accumulate


def solve(N, K, X, A):
    A = sorted(A, reverse=True)
    accA = list(accumulate(A, initial=0))

    if accA[N] - accA[N - K] < X:
        return -1

    ng = N - K
    ok = N
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if accA[mid] - accA[N - K] >= X:
            ok = mid
        else:
            ng = mid

    return ok


def main():
    N, K, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, K, X, A)
    print(ans)


if __name__ == "__main__":
    main()
