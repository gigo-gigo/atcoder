from collections import Counter, defaultdict
from math import isqrt


class Top:
    def __init__(self):
        self.first = 0
        self.second = 0

    def update(self, c):
        if c > self.first:
            self.second = self.first
            self.first = c
        elif c > self.second:
            self.second = c


def sieve(N):
    is_primes = [True] * (N + 1)
    is_primes[0] = False
    is_primes[1] = False
    q = 2
    while q * q <= N:
        if is_primes[q]:
            for qq in range(q + q, N + 1, q):
                is_primes[qq] = False
        q += 1

    primes = [p for p, is_prime in enumerate(is_primes) if is_prime]

    return primes


def factorize(x):
    p2r = Counter()
    for i in range(2, isqrt(x) + 1):
        while x % i == 0:
            p2r[i] += 1
            x //= i
    if x > 1:
        p2r[x] += 1

    return p2r


def solve(N, A, primes, MOD=998244353):
    Z = defaultdict(Top)
    P2R = []
    for a in A:
        p2r = Counter()
        for p in primes:
            r = 0
            while a % p == 0:
                r += 1
                a //= p
            if r > 0:
                p2r[p] = r
        if a > 1:
            p2r[a] = 1

        P2R.append(p2r)
        for k, v in p2r.items():
            Z[k].update(v)

    x = 1
    for p in Z.keys():
        r = Z[p].first
        x *= pow(p, r, MOD)
        x %= MOD

    ans = []
    for p2r in P2R:
        y = x
        for p, r in p2r.items():
            if r > Z[p].second:
                d = pow(p, Z[p].first - Z[p].second, MOD)
                y *= pow(d, -1, MOD)
                y %= MOD
        ans.append(y)

    return ans


def main():
    T = int(input())
    primes = sieve(3162)  # isqrt(10000000) = 3162
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = solve(N, A, primes)
        print(*ans)


if __name__ == "__main__":
    main()
