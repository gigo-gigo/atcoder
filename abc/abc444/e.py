from sortedcontainers import SortedList


def solve(N, D, A):
    ans = 0
    V = SortedList()
    V.add(10000000000)
    V.add(-10000000000)
    j = 0
    for i in range(N):
        if j <= i:
            V.add(A[i])
            j = i + 1
        while (
            j < N
            and (k := V.bisect_left(A[j]))
            and V[k] - A[j] >= D
            and A[j] - V[k - 1] >= D
        ):
            V.add(A[j])
            j += 1
        ans += j - i
        V.discard(A[i])

    return ans


def main():
    N, D = list(map(int, input().split()))
    A = list(map(int, input().split()))
    ans = solve(N, D, A)
    print(ans)


if __name__ == "__main__":
    main()
