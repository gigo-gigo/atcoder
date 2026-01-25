from collections import defaultdict
from functools import cmp_to_key
from itertools import accumulate
from math import gcd


def solve(N, X, Y, A, B):
    XX = []
    YY = []
    for x, y in zip(X, Y):
        g = gcd(abs(x), abs(y))
        x //= g
        y //= g
        if x == 0 and y > 0:
            x = 1
            y = 10000000000
        elif x == 0 and y < 0:
            x = 1
            y = -10000000000
        XX.append(x)
        YY.append(y)
    X = XX
    Y = YY

    Z = []
    i2n = [-1] * N

    D = defaultdict(list)
    for i, (x, y) in enumerate(zip(X, Y)):
        if x >= 0 and y <= 0:
            D[(x, y)].append(i)
    for key in sorted(
        D.keys(),
        key=cmp_to_key(lambda a, b: 1 if a[1] * b[0] < a[0] * b[1] else -1),
    ):
        for i in D[key]:
            i2n[i] = len(Z)
        Z.append(len(D[key]))

    D = defaultdict(list)
    for i, (x, y) in enumerate(zip(X, Y)):
        if x < 0 and y <= 0:
            D[(x, y)].append(i)
    for key in sorted(
        D.keys(),
        key=cmp_to_key(lambda a, b: 1 if a[1] * b[0] < a[0] * b[1] else -1),
    ):
        for i in D[key]:
            i2n[i] = len(Z)
        Z.append(len(D[key]))

    D = defaultdict(list)
    for i, (x, y) in enumerate(zip(X, Y)):
        if x < 0 and y > 0:
            D[(x, y)].append(i)
    for key in sorted(
        D.keys(),
        key=cmp_to_key(lambda a, b: 1 if a[1] * b[0] < a[0] * b[1] else -1),
    ):
        for i in D[key]:
            i2n[i] = len(Z)
        Z.append(len(D[key]))

    D = defaultdict(list)
    for i, (x, y) in enumerate(zip(X, Y)):
        if x >= 0 and y > 0:
            D[(x, y)].append(i)
    for key in sorted(
        D.keys(),
        key=cmp_to_key(lambda a, b: 1 if a[1] * b[0] < a[0] * b[1] else -1),
    ):
        for i in D[key]:
            i2n[i] = len(Z)
        Z.append(len(D[key]))

    Z = Z + Z
    accZ = list(accumulate(Z, initial=0))

    ans = []
    for a, b in zip(A, B):
        left = i2n[a]
        right = i2n[b]
        if right < left:
            right += len(Z) // 2
        right += 1
        x = accZ[right] - accZ[left]
        ans.append(x)

    return ans


def main():
    N, Q = list(map(int, input().split()))
    X = []
    Y = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    A = []
    B = []
    for _ in range(Q):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        A.append(a)
        B.append(b)
    ans = solve(N, X, Y, A, B)
    print(*ans)


if __name__ == "__main__":
    main()
