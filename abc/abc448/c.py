def solve(A, Bs):
    subA = sorted(A)[:6]

    ans = []
    for B in Bs:
        X = []
        for b in B:
            if b in subA:
                subA.remove(b)
                X.append(b)
        ans.append(min(subA))
        for b in X:
            subA.append(b)

    return ans


def main():
    N, Q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    Bs = []
    for _ in range(Q):
        _ = input()
        B = list(map(int, input().split()))
        B = [A[b - 1] for b in B]
        Bs.append(B)
    ans = solve(A, Bs)
    print(*ans)


if __name__ == "__main__":
    main()
