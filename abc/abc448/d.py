import sys
from collections import Counter

sys.setrecursionlimit(10**7)


def solve(N, A, G):
    def dfs(u, C, X, p=-1):
        C[A[u]] += 1
        if C[A[u]] == 2:
            X.add(A[u])

        if len(X) > 0:
            ans[u] = True

        for v in G[u]:
            if v != p:
                dfs(v, C, X, u)

        if C[A[u]] == 2:
            X.remove(A[u])
        C[A[u]] -= 1

    ans = [False] * N
    dfs(0, Counter(), set())

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = solve(N, A, G)
    for x in ans:
        print("Yes" if x else "No")


if __name__ == "__main__":
    main()
