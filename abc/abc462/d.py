def solve(N, D, S, T):
    imos = [0] * 3000000
    for s, t in zip(S, T):
        tt = max(s, t - D + 1)
        imos[s] += 1
        imos[tt] -= 1
    for i in range(1, 3000000):
        imos[i] += imos[i - 1]

    ans = sum(x * (x - 1) // 2 for x in imos)

    return ans


def main():
    N, D = list(map(int, input().split()))
    S = []
    T = []
    for _ in range(N):
        s, t = list(map(int, input().split()))
        S.append(s)
        T.append(t)
    ans = solve(N, D, S, T)
    print(ans)


if __name__ == "__main__":
    main()
