def solve(N, M, A, B, D):
    events = [[] for _ in range(M)]
    for a, b, d in zip(A, B, D):
        events[d].append((a, b))

    X = [0] * N
    for a in A:
        X[a] += 1
    c = sum(x > 0 for x in X)

    ans = [-1] * M
    for i, event in enumerate(events):
        for a, b in event:
            if a == b:
                continue
            X[a] -= 1
            X[b] += 1
            if X[a] == 0:
                c -= 1
            if X[b] == 1:
                c += 1
        ans[i] = c

    return ans


def main():
    N, M = list(map(int, input().split()))
    A = []
    D = []
    B = []
    for _ in range(N):
        a, d, b = list(map(int, input().split()))
        A.append(a - 1)
        D.append(d - 1)
        B.append(b - 1)
    ans = solve(N, M, A, B, D)
    print(*ans)


if __name__ == "__main__":
    main()
