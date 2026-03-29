from collections import deque
from math import log10


def solve(n, MAX=1000000000):
    P = [1 << i for i in range(30)]
    V = set()
    fifo = deque([0])
    while fifo:
        x = fifo.popleft()
        if x not in V and x <= MAX:
            V.add(x)
            for y in P:
                d = int(log10(y)) + 1
                z = pow(10, d) * x + y
                fifo.append(z)

    A = sorted(V)
    ans = A[n]

    return ans


def main():
    N = int(input())
    ans = solve(N)
    print(ans)


if __name__ == "__main__":
    main()
