from atcoder.dsu import DSU


def solve(N, queries):
    uf = DSU(N)
    C = [0] * N
    X = [0] * N
    ans = []
    for c, u, v in queries:
        if c == 1:
            if not uf.same(u, v):
                uu = uf.leader(u)
                vv = uf.leader(v)
                uf.merge(u, v)
                X[uf.leader(u)] = X[uu] + X[vv]
        elif c == 2:
            if C[u] == 0:
                X[uf.leader(u)] += 1
            else:
                X[uf.leader(u)] -= 1
            C[u] ^= 1
        else:
            f = X[uf.leader(u)] > 0
            ans.append("Yes" if f else "No")

    return ans


def main():
    N, Q = map(int, input().split())
    queries = []
    for _ in range(Q):
        c, *U = map(int, input().split())
        u, v = U[:2] if c == 1 else (U[0], -1)
        u -= 1
        v -= 1
        queries.append((c, u, v))
    ans = solve(N, queries)
    print(*ans)


if __name__ == "__main__":
    main()
