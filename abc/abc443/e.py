from collections import deque


def solve(N, C, S):
    sets = [[] for _ in range(N + 2)]
    for j in range(1, N + 1):
        for i in range(1, N + 1):
            if S[i][j] == "#":
                sets[j].append(i)

    X = [0] * (N + 2)
    fifo = deque([(N, C)])
    used = [[False] * (N + 2) for _ in range(N + 2)]
    used[N][C] = True
    while fifo:
        i, j = fifo.popleft()
        if i == 1:
            X[j] = 1
            continue
        ii = i - 1
        for jj in (j - 1, j, j + 1):
            if used[ii][jj]:
                continue
            if S[ii][jj] == ".":
                fifo.append((ii, jj))
                used[ii][jj] = True
            elif S[ii][jj] == "#":
                if sets[jj][-1] == ii:
                    sets[jj].pop()
                    fifo.append((ii, jj))
                    used[ii][jj] = True

    line = "".join(str(x) for x in X[1:-1])

    return line


def main():
    T = int(input())
    X = []
    for _ in range(T):
        N, C = list(map(int, input().split()))
        S = []
        S.append("@" * (N + 2))
        for _ in range(N):
            S.append(f"@{input()}@")
        S.append("@" * (N + 2))
        ans = solve(N, C, S)
        X.append(ans)
    for line in X:
        print(line)


if __name__ == "__main__":
    main()
