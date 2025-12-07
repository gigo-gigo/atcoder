from collections import deque


def solve(N, M, G, queries):
    costs = [-1] * N
    ans = []
    for c, v in queries:
        if c == 1:
            if costs[v] < 0:
                costs[v] = 0
                fifo = deque([v])
                while fifo:
                    v = fifo.popleft()
                    for u in G[v]:
                        if costs[u] < 0:
                            costs[u] = costs[v] + 1
                            fifo.append(u)
        else:
            ans.append(costs[v] >= 0)

    return ans


def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[v].append(u)
    queries = []
    Q = int(input())
    for _ in range(Q):
        c, v = map(int, input().split())
        v -= 1
        queries.append((c, v))
    ans = solve(N, M, G, queries)
    ans = ["Yes" if x else "No" for x in ans]
    print(*ans)


if __name__ == "__main__":
    main()
