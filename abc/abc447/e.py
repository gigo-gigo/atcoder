from atcoder.dsu import DSU


def solve(N, M, edges, MOD=998244353):
    uf = DSU(N)
    V = set()
    for i in range(M - 1, -1, -1):
        u, v = edges[i]
        if uf.same(u, v) or uf.size(u) + uf.size(v) < N:
            uf.merge(u, v)
            V.add(i)

    ans = 0
    for i in range(M):
        if i not in V:
            ans += pow(2, i + 1, MOD)
            ans %= MOD

    return ans


def main():
    N, M = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        edges.append((u, v))
    ans = solve(N, M, edges)
    print(ans)


if __name__ == "__main__":
    main()
