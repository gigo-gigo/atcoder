from math import isqrt


def solve(N):
    C = [0] * (N + 1)
    for y in range(2, isqrt(N) + 1):
        for x in range(1, min(y, isqrt(N - y * y) + 1)):
            n = x * x + y * y
            C[n] += 1

    ans = sorted(i for i, c in enumerate(C) if c == 1)

    return ans


def main():
    N = int(input())
    ans = solve(N)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
