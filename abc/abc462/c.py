def solve(N, X, Y):
    Ys = [[] for _ in range(N + 1)]
    for x, y in zip(X, Y):
        Ys[x].append(y)

    ans = 0
    y_min = N + 1
    for Y in Ys:
        ans += sum(y > y_min for y in Y)
        for y in Y:
            y_min = min(y_min, y)

    return N - ans


def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)
    ans = solve(N, X, Y)
    print(ans)


if __name__ == "__main__":
    main()
