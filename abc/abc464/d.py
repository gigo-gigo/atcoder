def solve(N, S, X, Y):
    dp = [0] * 2
    if S[0] == "S":
        dp[1] = -X[0]
    else:
        dp[0] = -X[0]

    for s, x, y in zip(S[1:], X[1:], Y):
        ep = [-200000000000000] * 2
        if s == "S":
            ep[0] = max(dp[0], dp[1] + y)
            ep[1] = max(dp[0] - x, dp[1] - x)
        else:
            ep[0] = max(dp[0] - x, dp[1] - x + y)
            ep[1] = max(dp[0], dp[1])
        dp = ep
    ans = max(dp)

    return ans


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        S = input()
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))
        z = solve(N, S, X, Y)
        ans.append(z)
    print(*ans)


if __name__ == "__main__":
    main()
