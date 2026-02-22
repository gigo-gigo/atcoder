from collections import deque


def solve(N, D, A, B):
    fifo = deque()
    for i, (a, b) in enumerate(zip(A, B), 1):
        for _ in range(a):
            fifo.append(i + D)
        while fifo and b > 0:
            if fifo[0] >= i:
                b -= 1
            fifo.popleft()
        while fifo and fifo[0] <= i:
            fifo.popleft()

    ans = len(fifo)

    return ans


def main():
    T = int(input())
    X = []
    for _ in range(T):
        N, D = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        x = solve(N, D, A, B)
        X.append(x)
    print(*X)


if __name__ == "__main__":
    main()
