from itertools import accumulate


def solve(N, A, queries):
    accA = list(accumulate(A, initial=0))
    ans = []
    for c, left, right in queries:
        if c == 1:
            accA[left + 1] += -A[left] + A[left + 1]
            A[left], A[left + 1] = A[left + 1], A[left]
        else:
            x = accA[right] - accA[left]
            ans.append(x)

    return ans


def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        c, *X = list(map(int, input().split()))
        left, right = (X[0] - 1, -1) if c == 1 else (X[0] - 1, X[1])
        queries.append((c, left, right))
    ans = solve(N, A, queries)
    print(*ans)


if __name__ == "__main__":
    main()
