from collections import defaultdict, deque
from itertools import chain


def solve(H, W, S):
    start = -1
    goal = -1
    for i in range(H + 2):
        for j in range(W + 2):
            x = i * (W + 2) + j
            if S[x] == "S":
                start = x
            elif S[x] == "G":
                goal = x

    dx2i = {1: 0, W + 2: 1, -1: 2, -(W + 2): 3}
    i2dx = [1, W + 2, -1, -(W + 2)]
    dx2command = {1: "R", W + 2: "D", -1: "L", -(W + 2): "U"}

    fifo = deque([(start, 1), (start, W + 2), (start, -1), (start, -(W + 2))])
    pa = [-1] * ((H + 2) * (W + 2) * 4)
    while fifo:
        x, dx = fifo.popleft()
        if x == goal:
            break
        xx = x + dx
        if S[xx] == "o":
            if pa[4 * xx + dx2i[dx]] == -1:
                fifo.append((xx, dx))
                pa[4 * xx + dx2i[dx]] = 4 * x + dx2i[dx]
        elif S[xx] == "x":
            for ndx in [1, W + 2, -1, -(W + 2)]:
                if ndx != dx and pa[4 * xx + dx2i[ndx]] == -1:
                    fifo.append((xx, ndx))
                    pa[4 * xx + dx2i[ndx]] = 4 * x + dx2i[dx]
        elif S[xx] == "." or S[xx] == "G":
            for ndx in [1, W + 2, -1, -(W + 2)]:
                if pa[4 * xx + dx2i[ndx]] == -1:
                    fifo.append((xx, ndx))
                    pa[4 * xx + dx2i[ndx]] = 4 * x + dx2i[dx]

    ans = []
    for ndx in [1, W + 2, -1, -(W + 2)]:
        if pa[4 * goal + dx2i[ndx]] >= 0:
            xx = goal
            while pa[4 * xx + dx2i[ndx]] >= 0:
                X = pa[4 * xx + dx2i[ndx]]
                x, dx = X // 4, i2dx[X % 4]
                ans.append(dx2command[dx])
                xx, ndx = x, dx

            return tuple(ans[::-1])

    return tuple()


def main():
    H, W = list(map(int, input().split()))
    S = []
    S.append("#" * (W + 2))
    for _ in range(H):
        row = "#" + input() + "#"
        S.append(row)
    S.append("#" * (W + 2))
    S = list(chain.from_iterable(S))
    ans = solve(H, W, S)
    if ans:
        print("Yes")
        print("".join(ans))
    else:
        print("No")


if __name__ == "__main__":
    main()
