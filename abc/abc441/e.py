from itertools import accumulate

from sortedcontainers import SortedList


def solve(N, S):
    A = list(accumulate([int(s == "A") for s in S], initial=0))
    B = list(accumulate([int(s == "B") for s in S], initial=0))
    D = [a - b for a, b in zip(A, B)]

    ans = 0
    sl = SortedList()
    for d in D:
        ans += sl.bisect_left(d)
        sl.add(d)

    return ans


def main():
    N = int(input())
    S = input()
    ans = solve(N, S)
    print(ans)


if __name__ == "__main__":
    main()
