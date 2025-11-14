from sortedcontainers import SortedSet


def solve(N, X, MAX=10000000000):
    ss = SortedSet([-MAX, 0, X[0], MAX])
    d = 2 * X[0]
    ans = [d]
    for x in X[1:]:
        i = ss.bisect_left(x)

        d -= min(ss[i - 1] - ss[i - 2], ss[i] - ss[i - 1])
        d += min(ss[i - 1] - ss[i - 2], x - ss[i - 1])

        if ss[i] < MAX:
            d -= min(ss[i] - ss[i - 1], ss[i + 1] - ss[i])
            d += min(ss[i + 1] - ss[i], ss[i] - x)

        d += min(x - ss[i - 1], ss[i] - x)

        ans.append(d)
        ss.add(x)

    return ans


def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = solve(N, X)
    print(*ans)


if __name__ == "__main__":
    main()
