from heapq import heappop, heappush


def solve(queries):
    ans = []
    heap = []
    for c, h in queries:
        if c == 1:
            heappush(heap, h)
        else:
            while heap and heap[0] <= h:
                heappop(heap)
        ans.append(len(heap))

    return ans


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        c, h = list(map(int, input().split()))
        queries.append((c, h))
    ans = solve(queries)
    print(*ans)


if __name__ == "__main__":
    main()
