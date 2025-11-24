def solve(N, M, edges):
    def generate_bipartite_graph(colors):
        V = []
        for u, v in edges:
            if colors[u] != colors[v]:
                V.append((u, v))

        return V

    ans = M
    for p in range(1 << N):
        colors = []
        q = p
        for _ in range(N):
            colors.append(q & 1)
            q >>= 1

        V = generate_bipartite_graph(colors)
        ans = min(ans, len(edges) - len(V))

    return ans


def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
    ans = solve(N, M, edges)
    print(ans)


if __name__ == "__main__":
    main()
