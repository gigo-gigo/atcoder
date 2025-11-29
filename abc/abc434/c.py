def solve(N, H, A):
    t0 = 0
    l0 = H
    u0 = H
    for t1, l1, u1 in A:
        l = max(max(0, l0 - (t1 - t0)), l1)
        u = min(max(0, u0 + (t1 - t0)), u1)
        l0 = l
        u0 = u
        t0 = t1
        if l > u:
            return False

    return True


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        N, H = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(N)]
        x = solve(N, H, A)
        ans.append("Yes" if x else "No")
    print(*ans)


if __name__ == "__main__":
    main()
