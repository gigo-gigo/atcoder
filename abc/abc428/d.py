from math import isqrt


def solve(c, d):
    ans = 0
    for digit in range(1, 11):
        left = max(1, pow(10, digit - 1) - c)
        right = min(d, pow(10, digit) - 1 - c)
        if right >= left:
            m = isqrt(c * pow(10, digit) + c + right) - isqrt(
                c * pow(10, digit) + c + left - 1
            )
            ans += m

    return ans


def main():
    T = int(input())

    ans = []
    for _ in range(T):
        c, d = list(map(int, input().split()))
        x = solve(c, d)
        ans.append(x)
    print(*ans)


if __name__ == "__main__":
    main()
