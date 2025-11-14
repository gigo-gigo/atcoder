from bisect import bisect_left
from itertools import accumulate


def solve(N, A, B, S):
    X = [int(s == "a") for s in S]
    Y = [int(s != "a") for s in S]
    accX = list(accumulate(X, initial=0))
    accY = list(accumulate(Y, initial=0))

    ans = 0
    for left in range(N):
        i = bisect_left(accX, accX[left] + A)
        j = bisect_left(accY, accY[left] + B)
        ans += max(0, j - i)

    return ans


def main():
    N, A, B = list(map(int, input().split()))
    S = input()
    ans = solve(N, A, B, S)
    print(ans)


if __name__ == "__main__":
    main()
