def solve(N):
    def f(x):
        total = 0
        while x > 0:
            total += pow(x % 10, 2)
            x //= 10

        return total

    costs = [-1] * 10000
    costs[N] = 0
    x = N
    while costs[xx := f(x)] == -1:
        costs[xx] = costs[x] + 1
        x = xx

    return costs[1] >= 0


def main():
    N = int(input())
    ans = "Yes" if solve(N) else "No"
    print(ans)


if __name__ == "__main__":
    main()
