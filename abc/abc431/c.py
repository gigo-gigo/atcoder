from heapq import heappop, heappush


def solve1(N, M, K, H, B):
    heapH = []
    for h in H:
        heappush(heapH, h)

    heapB = []
    for b in B:
        heappush(heapB, b)

    pairs = []
    while heapH and heapB:
        if heapH[0] <= heapB[0]:
            h = heappop(heapH)
            b = heappop(heapB)
            pairs.append((h, b))
        else:
            heappop(heapB)

    return pairs


def solve2(N, M, K, H, B):
    H = sorted(H)
    B = sorted(B)

    pairs = []
    i = 0
    for b in B:
        if i < N and H[i] <= b:
            pairs.append((H[i], b))
            i += 1

    return pairs


def main():
    N, M, K = map(int, input().split())
    H = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # pairs = solve1(N, M, K, H, B)
    pairs = solve2(N, M, K, H, B)
    ans = "Yes" if len(pairs) >= K else "No"
    # print(pairs)
    print(ans)


if __name__ == "__main__":
    main()
