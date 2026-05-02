def solve(N, A):
    ans = 0
    for i in range(1 << N):
        j = i
        x = 0
        c = 0
        for dx in A:
            xx = x + (dx if j & 1 else -dx)
            if x >= 0 and xx < 0 or x < 0 and xx >= 0:
                c += 1
            x = xx
            j >>= 1
        ans = max(ans, c)

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
