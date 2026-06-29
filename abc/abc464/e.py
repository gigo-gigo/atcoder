def solve(H, W, Q, R, C, X):
    lines = [[Q] * W for _ in range(H)]
    for i in range(Q):
        for r in range(R[i], -1, -1):
            if lines[r][C[i]] < i:
                break
            for c in range(C[i], -1, -1):
                if lines[r][c] < i:
                    break
                lines[r][c] = i

    S = [["A"] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            S[r][c] = X[lines[r][c]]

    ans = "\n".join(["".join(line) for line in S])

    return ans


def main():
    H, W, Q = list(map(int, input().split()))
    R = [H - 1]
    C = [W - 1]
    X = ["A"]
    for _ in range(Q):
        r, c, x = input().split()
        r = int(r) - 1
        c = int(c) - 1
        R.append(r)
        C.append(c)
        X.append(x)
    R = R[::-1]
    C = C[::-1]
    X = X[::-1]
    ans = solve(H, W, Q, R, C, X)
    print(ans)


if __name__ == "__main__":
    main()
