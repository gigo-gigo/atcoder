from functools import cache


def solve1(N, M, K, S, G):

    @cache
    def dfs(i=0, u=0):
        if i == 2 * K:
            return S[u] == "A"

        if i & 1:
            return not any(not dfs(i + 1, v) for v in G[u])
        else:
            return any(dfs(i + 1, v) for v in G[u])

    ans = "Alice" if dfs() else "Bob"

    return ans


def solve2(N, M, K, S, G):
    result = {}
    lifo = [(~0, 0), (0, 0)]
    while lifo:
        u, k = lifo.pop()
        if u >= 0:
            if (u, k) in result:
                continue

            if k < 2 * K:
                for v in G[u]:
                    lifo.append((~v, k + 1))
                    lifo.append((v, k + 1))
        else:
            u = ~u
            if (u, k) in result:
                continue

            if k == 2 * K:
                result[(u, k)] = S[u] == "A"
            else:
                if k & 1:
                    result[(u, k)] = not any(not result[(v, k + 1)] for v in G[u])
                else:
                    result[(u, k)] = any(result[(v, k + 1)] for v in G[u])

    ans = "Alice" if result[(0, 0)] else "Bob"

    return ans


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N, M, K = map(int, input().split())
        S = input()
        G = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            G[u].append(v)
        x = solve2(N, M, K, S, G)
        ans.append(x)
    print(*ans)


if __name__ == "__main__":
    main()
