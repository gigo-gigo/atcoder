from itertools import pairwise

from more_itertools import run_length


def solve(S):
    ans = 0
    for (s, n), (t, m) in pairwise(run_length.encode(S)):
        if s + 1 == t:
            ans += min(n, m)

    return ans


def main():
    S = input()
    S = [int(s) for s in S]
    ans = solve(S)
    print(ans)


if __name__ == "__main__":
    main()
