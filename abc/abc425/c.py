from itertools import accumulate
from operator import add

from atcoder.segtree import SegTree


def solve1(N, A, queries):
    seg = SegTree(add, 0, A)
    top = 0

    ans = []
    for c, left, right in queries:
        if c == 1:
            top += left
            top %= N
        else:
            if top + left >= N:
                x = seg.prod((top + left) % N, (top + right) % N)
            elif top + right > N:
                x = seg.prod(top + left, N) + seg.prod(0, (top + right) % N)
            else:
                x = seg.prod(top + left, top + right)
            ans.append(x)

    return ans


def solve2(N, A, queries):
    AA = A + A[:-1]
    accAA = list(accumulate(AA, initial=0))
    top = 0

    ans = []
    for c, left, right in queries:
        if c == 1:
            top += left
            top %= N
        else:
            x = accAA[top + right] - accAA[top + left]
            ans.append(x)

    return ans


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        c, *X = map(int, input().split())
        if len(X) == 1:
            left = X[0]
            right = -1
        else:
            left, right = X[:2]
            left -= 1
        queries.append((c, left, right))
    ans = solve2(N, A, queries)
    print(*ans)


if __name__ == "__main__":
    main()
