import sys

sys.setrecursionlimit(10**7)


def solve(m, a, b):
    def dfs(u):
        if used[u]:
            return X[u]
        if X[u]:
            used[u] = True
            return X[u]

        used[u] = True
        X[u] |= dfs(A[u])

        return X[u]

    A = [-1] * (m * m)
    for x in range(m):
        for y in range(m):
            u = y * m + x
            z = (a * y % m + b * x % m) % m
            v = z * m + y
            A[u] = v

    X = [False] * (m * m)
    for x in range(m):
        for y in range(m):
            u = y * m + x
            if x % m == 0 or y % m == 0:
                X[u] = True

    used = [False] * (m * m)
    for x in range(m):
        for y in range(m):
            u = y * m + x
            dfs(u)

    ans = m * m - sum(X)

    return ans


def main():
    m, a, b = list(map(int, input().split()))
    ans = solve(m, a, b)
    print(ans)


if __name__ == "__main__":
    main()
