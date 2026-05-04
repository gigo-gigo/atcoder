def solve(S, MOD=998244353):
    dp = [0] * 3
    for s in S:
        ep = list(dp)
        for t in range(3):
            if t != s:
                ep[s] += dp[t]
                ep[s] %= MOD
        ep[s] += 1
        ep[s] %= MOD
        dp = ep

    ans = sum(dp) % MOD

    return ans


def main():
    S = input()
    S = [ord(s) - ord("a") for s in S]
    ans = solve(S)
    print(ans)


if __name__ == "__main__":
    main()
