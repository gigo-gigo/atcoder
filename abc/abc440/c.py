from itertools import accumulate


def solve(N, W, C):
    X = [0] * (2 * W)
    for i, c in enumerate(C):
        X[i % (2 * W)] += c

    XX = X + X
    accXX = list(accumulate(XX, initial=0))

    ans = float("inf")
    for i in range(2 * W):
        ans = min(ans, accXX[i + W] - accXX[i])

    return ans


def main():
    T = int(input())
    for _ in range(T):
        N, W = list(map(int, input().split()))
        C = list(map(int, input().split()))
        ans = solve(N, W, C)
        print(ans)


if __name__ == "__main__":
    main()
