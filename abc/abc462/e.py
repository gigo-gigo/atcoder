def solve(a, b, x, y):
    col = abs(x)
    row = abs(y)
    n = min(col, row)
    m = max(col, row) - n

    c = min(a * n + a * n, b * n + b * n)
    if col > row:
        c1 = a * ((m + 1) // 2) + b * (m // 2)
        c2 = a * m + a * (m // 2 * 2)
        c3 = b * m + b * ((m + 1) // 2 * 2)
        ans = c + min(c1, c2, c3)
    else:
        c1 = b * ((m + 1) // 2) + a * (m // 2)
        c2 = b * m + b * (m // 2 * 2)
        c3 = a * m + a * ((m + 1) // 2 * 2)
        ans = c + min(c1, c2, c3)

    return ans


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        a, b, x, y = list(map(int, input().split()))
        z = solve(a, b, x, y)
        ans.append(z)
    print(*ans)


if __name__ == "__main__":
    main()
