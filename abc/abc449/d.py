def f(x, ymin, ymax):
    if x < 0:
        return 0

    b = 0
    for y in range(ymin, ymax + 1):
        y = abs(y)
        if y > x:
            b += x + 1 if y % 2 == 0 else 0
        else:
            b += y + 1 if y % 2 == 0 else 0
            b += (x + 2) // 2 - (y + 2) // 2

    return b


def solve(L, R, D, U):
    if L >= 0:
        return f(R, D, U) - f(L - 1, D, U)
    elif R <= 0:
        return f(-L, D, U) - f(-R - 1, D, U)
    else:
        return f(R, D, U) + f(-L, D, U) - f(0, D, U)


def main():
    L, R, D, U = list(map(int, input().split()))
    ans = solve(L, R, D, U)
    print(ans)


if __name__ == "__main__":
    main()
