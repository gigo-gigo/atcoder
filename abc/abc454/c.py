from collections import deque


def solve(N, M, G):
    used = set([0])
    fifo = deque([0])
    while fifo:
        u = fifo.popleft()
        for v in G[u]:
            if v not in used:
                used.add(v)
                fifo.append(v)

    return len(used)


def main():
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        G[a].append(b)
    ans = solve(N, M, G)
    print(ans)


if __name__ == "__main__":
    main()
