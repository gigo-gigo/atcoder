from itertools import chain


def solve(H, W, S):
    def is_valid(x):
        num_blacks = sum((x + dx) in blacks for dx in [1, W + 2, -1, -W - 2])
        return num_blacks == 1

    blacks = set()
    for x, s in enumerate(S):
        if s == "#":
            blacks.add(x)
    new_blacks = set(blacks)

    while new_blacks:
        next_blacks = set()
        for x in new_blacks:
            for dx in [1, W + 2, -1, -W - 2]:
                xx = x + dx
                if S[xx] != "@" and xx not in blacks and is_valid(xx):
                    next_blacks.add(xx)
        new_blacks = next_blacks
        blacks |= new_blacks

    return len(blacks)


def main():
    H, W = map(int, input().split())
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
