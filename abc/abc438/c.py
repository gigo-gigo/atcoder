from more_itertools import run_length


def f(N, A):
    lifo = [(0, 0)]
    for a, m in run_length.encode(A):
        m0 = 0
        if lifo[-1][0] == a:
            _, m0 = lifo.pop()
        m0 += m
        if (m1 := m0 % 4) > 0:
            lifo.append((a, m1))

    ans = sum(m for _, m in lifo)

    return ans


def solve(N, A):
    ans = min(f(N, A), f(N, A[::-1]))

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
