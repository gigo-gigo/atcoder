def solve(N, M, G):
    X = []
    for i in range(N):
        n = N - len(G[i]) - 1
        x = n * (n - 1) * (n - 2) // 6
        X.append(x)

    return X


def main():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = solve(N, M, G)
    print(*ans)


if __name__ == "__main__":
    main()
