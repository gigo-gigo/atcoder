from collections import defaultdict


def solve(H, W, N, squares):
    h2hw = defaultdict(set)
    w2hw = defaultdict(set)
    for i, (h, w) in enumerate(squares):
        h2hw[h].add((h, w, i))
        w2hw[w].add((h, w, i))

    ans = [[-1, -1] for _ in range(N)]
    n = 0
    while n < N:
        if len(h2hw[H]) > 0:
            h, w, i = h2hw[H].pop()
            ans[i][0] = 0
            ans[i][1] = W - w
            W -= w
            w2hw[w].discard((h, w, i))
            n += 1
        else:
            h, w, i = w2hw[W].pop()
            ans[i][0] = H - h
            ans[i][1] = 0
            H -= h
            h2hw[h].discard((h, w, i))
            n += 1

    for i in range(N):
        ans[i][0] += 1
        ans[i][1] += 1

    return ans


def main():
    H, W, N = list(map(int, input().split()))
    squares = []
    for _ in range(N):
        h, w = list(map(int, input().split()))
        squares.append((h, w))
    ans = solve(H, W, N, squares)
    for x, y in ans:
        print(x, y)


if __name__ == "__main__":
    main()
