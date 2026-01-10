from bisect import bisect_left, bisect_right


def solve(N, A, queries):
    A = sorted(A)

    ans = []
    for x, y in queries:
        base = bisect_left(A, x)
        ok = 2000000001
        ng = x + y - 2
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if (mid - x + 1) - (bisect_right(A, mid) - base) >= y:
                ok = mid
            else:
                ng = mid
        ans.append(ok)

    return ans


def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        x, y = list(map(int, input().split()))
        queries.append((x, y))
    ans = solve(N, A, queries)
    for x in ans:
        print(x)


if __name__ == "__main__":
    main()
