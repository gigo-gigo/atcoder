from atcoder.scc import SCCGraph


def solve(N, A):
    A = [0] + A

    B = [-1] * (N + 1)
    for i, a in enumerate(A):
        B[a] = i

    G = SCCGraph(N + 1)
    for i, a in enumerate(A):
        G.add_edge(i, a)

    X = [-1] * (N + 1)
    for group in G.scc()[::-1]:
        if len(group) > 1 or len(group) == 1 and group[0] == A[group[0]]:
            u = group[0]
            i = pow(10, 100, len(group))
            v = group[i]
            X[u] = v
            while X[A[u]] == -1:
                X[A[u]] = A[v]
                u, v = A[u], A[v]
        else:
            u = group[0]
            v = A[u]
            vv = X[v]
            uu = B[vv]
            X[u] = X[uu]

    return X[1:]


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(*ans)


if __name__ == "__main__":
    main()
