def solve(N, W, H, B, MAX=250501):
    dp = [-1] * MAX
    sumW = sum(W)
    dp[sumW] = sum(B)
    for w, h, b in zip(W, H, B):
        for bw in range(250001):
            hw = sumW - bw
            if dp[bw + w] >= 0 and bw >= hw >= 0:
                dp[bw] = max(dp[bw], dp[bw + w] - b + h)

    ans = max(dp)

    return ans


def main():
    N = int(input())
    W = []
    H = []
    B = []
    for _ in range(N):
        w, h, b = map(int, input().split())
        W.append(w)
        H.append(h)
        B.append(b)
    ans = solve(N, W, H, B)
    print(ans)


if __name__ == "__main__":
    main()
