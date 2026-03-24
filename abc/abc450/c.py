from itertools import chain

from atcoder.dsu import DSU


def solve(H, W, S):
    uf = DSU((H + 2) * (W + 2))
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            x = i * (W + 2) + j
            if S[x] == "#":
                continue
            for dx in [1, W + 2, -1, -(W + 2)]:
                xx = x + dx
                if S[xx] != "#":
                    uf.merge(x, xx)
    for j in range(W + 1):
        uf.merge(j, j + 1)
        uf.merge(j + (H + 1) * (W + 2), j + 1 + (H + 1) * (W + 2))
    for i in range(H + 1):
        uf.merge(i * (W + 2), (i + 1) * (W + 2))
        uf.merge(i * (W + 2) + W + 1, (i + 1) * (W + 2) + W + 1)

    V = set()
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            x = i * (W + 2) + j
            if S[x] == ".":
                V.add(uf.leader(x))

    ans = len(V) - int(uf.size(0) > 2 * (W + 2) + 2 * (H + 2) - 4)

    return ans


def main():
    H, W = list(map(int, input().split()))
    S = []
    S.append("@" * (W + 2))
    for _ in range(H):
        S.append("@" + input() + "@")
    S.append("@" * (W + 2))
    S = list(chain.from_iterable(S))
    ans = solve(H, W, S)
    print(ans)


if __name__ == "__main__":
    main()
