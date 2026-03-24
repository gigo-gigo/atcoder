def solve(N, K, A):
    B = sorted([a % K for a in A])
    BB = B + [b + K for b in B]
    ans = min(BB[i + N - 1] - BB[i] for i in range(N))

    return ans


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, K, A)
    print(ans)


if __name__ == "__main__":
    main()
