import sys

sys.setrecursionlimit(10**7)


def solve1(N, M, L, S, T, G):
    def dfs(u=0, x=0, cost=0):
        if x >= L:
            if S <= cost <= T:
                yield u
            return

        for v, c in G[u]:
            yield from dfs(v, x + 1, cost + c)

    ans = set(dfs())
    ans = [u + 1 for u in sorted(ans)]

    return ans


def solve2(N, M, L, S, T, G):
    X = [0] * N

    lifo = [(0, 0, 0)]
    while lifo:
        u, x, cost = lifo.pop()
        if x >= L:
            if S <= cost <= T:
                X[u] += 1
            continue

        for v, c in G[u]:
            lifo.append((v, x + 1, cost + c))

    ans = [u for u, x in enumerate(X, 1) if x > 0]

    return ans


def main():
    N, M, L, S, T = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, c = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append((v, c))
    ans = solve2(N, M, L, S, T, G)
    print(*ans)


if __name__ == "__main__":
    main()
