from collections import defaultdict, deque
from itertools import chain


def solve(H, W, S):
    start = ((W + 2) + 1, 1)
    goal = ((W + 2) * H + W + 1, 1)

    dq = deque()
    dq.append(start)
    costs = defaultdict(lambda: float("inf"))
    costs[start] = 0
    while dq:
        x, dx = dq.popleft()
        if S[x] == "A":
            dx0 = dx
        elif S[x] == "B":
            dx0 = (W + 2) if dx == 1 or dx == -1 else 1
            dx0 *= 2 * int(dx > 0) - 1
        elif S[x] == "C":
            dx0 = -(W + 2) if dx == 1 or dx == -1 else -1
            dx0 *= 2 * int(dx > 0) - 1
        else:
            continue

        if costs[(x, dx)] < costs[(x + dx0, dx0)]:
            costs[(x + dx0, dx0)] = costs[(x, dx)]
            dq.appendleft((x + dx0, dx0))

        DX = set([1, -1, W + 2, -W - 2])
        DX.discard(-dx)
        DX.discard(dx0)
        for dx1 in DX:
            if costs[(x, dx)] + 1 < costs[(x + dx1, dx1)]:
                costs[(x + dx1, dx1)] = costs[(x, dx)] + 1
                dq.append((x + dx1, dx1))

    ans = costs[goal]

    return ans


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        H, W = map(int, input().split())
        S = []
        S.append("@" * (W + 2))
        for _ in range(H):
            S.append("@" + input() + "@")
        S.append("@" * (W + 2))
        S = "".join(chain(S))
        x = solve(H, W, S)
        ans.append(x)
    print(*ans)


if __name__ == "__main__":
    main()
