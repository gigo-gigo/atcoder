from atcoder.scc import SCCGraph


def solve(N, W, edges, S):
    G = SCCGraph(N * W)
    for u, v in edges:
        for w in range(W):
            ww = (w + 1) % W
            if S[u][w] == "o" and S[v][ww] == "o":
                G.add_edge(u * W + w, v * W + ww)
            if S[v][w] == "o" and S[u][ww] == "o":
                G.add_edge(v * W + w, u * W + ww)
    for u in range(N):
        for w in range(W):
            ww = (w + 1) % W
            if S[u][w] == "o" and S[u][ww] == "o":
                G.add_edge(u * W + w, u * W + ww)

    return any(len(group) > 1 for group in G.scc())


def main():
    T = int(input())
    X = []
    for _ in range(T):
        N, M = list(map(int, input().split()))
        edges = []
        for _ in range(M):
            u, v = list(map(int, input().split()))
            edges.append((u - 1, v - 1))
        W = int(input())
        S = [input() for _ in range(N)]
        ans = "Yes" if solve(N, W, edges, S) else "No"
        X.append(ans)
    print(*X)


if __name__ == "__main__":
    main()
