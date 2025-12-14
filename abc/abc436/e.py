from atcoder.scc import SCCGraph


def solve(N, P):
    G = SCCGraph(N)
    for i, p in enumerate(P):
        G.add_edge(i, p)

    ans = 0
    for group in G.scc():
        m = len(group)
        ans += m * (m - 1) // 2

    return ans


def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [p - 1 for p in P]
    ans = solve(N, P)
    print(ans)


if __name__ == "__main__":
    main()
