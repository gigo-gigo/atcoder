def solve(N, T, A):
    tau = -100
    ans = 0
    for a in A:
        if a - tau < 100:
            continue
        tau += 100
        ans += a - tau
        tau = a
    tau += 100
    ans += max(0, T - tau)

    return ans


def main():
    N, T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, T, A)
    print(ans)


if __name__ == "__main__":
    main()
