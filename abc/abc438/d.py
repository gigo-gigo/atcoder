from itertools import accumulate


def solve(N, A, B, C):
    accA = list(accumulate(A, initial=0))
    accB = list(accumulate(B, initial=0))
    accC = list(accumulate(C, initial=0))

    # 1 <= x < N - 1, x + 1 <= y < N,
    # total = (accA[x] - accA[0]) + (accB[y] - accB[x]) + (accC[N] - accC[y])
    # total = (accA[x] - accB[x]) + (accB[y] - accC[y]) + accC[N]

    ans = 0
    z = -float("inf")
    for y in range(2, N):
        z = max(z, accA[y - 1] - accB[y - 1])
        total = z + (accB[y] - accC[y]) + accC[N]
        ans = max(ans, total)

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = solve(N, A, B, C)
    print(ans)


if __name__ == "__main__":
    main()
