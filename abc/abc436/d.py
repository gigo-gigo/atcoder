from collections import defaultdict, deque
from itertools import chain


def solve(H, W, S: list[str], start, goal):
    costs = [float("inf")] * ((H + 2) * (W + 2))
    costs[start] = 0
    fifo = deque([start])
    x2warps = defaultdict(list)
    for x, s in enumerate(S):
        if s.isalpha():
            x2warps[s].append(x)

    while fifo:
        x = fifo.popleft()
        for dx in [-1, 1, -(W + 2), W + 2]:
            xx = x + dx
            if S[xx] != "#" and costs[xx] > costs[x] + 1:
                costs[xx] = costs[x] + 1
                fifo.append(xx)
        if S[x].isalpha() and S[x] in x2warps:
            for xx in x2warps[S[x]]:
                if costs[xx] > costs[x] + 1:
                    costs[xx] = costs[x] + 1
                    fifo.append(xx)
            x2warps[S[x]] = []

    ans = -1 if costs[goal] == float("inf") else costs[goal]

    return ans


def main():
    H, W = map(int, input().split())
    S = []
    S.append("#" * (W + 2))
    for _ in range(H):
        row = "#" + input() + "#"
        S.append(row)
    S.append("#" * (W + 2))
    S = list(chain.from_iterable(S))
    ans = solve(H, W, S, W + 3, H * (W + 2) + W)
    print(ans)


if __name__ == "__main__":
    main()
