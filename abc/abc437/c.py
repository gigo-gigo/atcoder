from bisect import bisect_right
from itertools import accumulate


def solve(N, W, P):
    WP = sorted(w + p for w, p in zip(W, P))
    accWP = list(accumulate(WP))
    return bisect_right(accWP, sum(P))


def main():
    T = int(input())
    X = []
    for _ in range(T):
        N = int(input())
        W = []
        P = []
        for _ in range(N):
            w, p = map(int, input().split())
            W.append(w)
            P.append(p)
        ans = solve(N, W, P)
        X.append(ans)
    print(*X)


if __name__ == "__main__":
    main()
