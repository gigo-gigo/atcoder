from bisect import bisect_left
from itertools import accumulate


def solve(N, M, A, B, MOD=998244353):
    A = sorted(A)
    B = sorted(B)
    accB = list(accumulate(B, initial=0))

    ans = 0
    for a in A:
        i = bisect_left(B, a)
        ans += (i * a) % MOD
        ans %= MOD
        ans += -(accB[i] - accB[0]) % MOD
        ans %= MOD
        ans += -(M - i) * a % MOD
        ans %= MOD
        ans += (accB[M] - accB[i]) % MOD
        ans %= MOD

    return ans


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = solve(N, M, A, B)
    print(ans)


if __name__ == "__main__":
    main()
