from heapq import heappop, heappush


def solve(N, A):
    heap = []
    for i, a in enumerate(A):
        heappush(heap, (a, i))

    B = list(A)
    visited = [False] * N
    while heap:
        a, i = heappop(heap)
        if visited[i]:
            continue
        visited[i] = True
        J = []
        if i > 0 and B[i - 1] > B[i]:
            J.append(i - 1)
        if i < N - 1 and B[i + 1] > B[i]:
            J.append(i + 1)
        for j in J:
            d = B[j] - B[i]
            B[j] -= d - 1
            heappush(heap, (B[j], j))

    ans = sum(a - b for a, b in zip(A, B))

    return ans


def main():
    T = int(input())
    X = []
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        ans = solve(N, A)
        X.append(ans)
    print(*X)


if __name__ == "__main__":
    main()
