def solve(N, A):
    A = sorted(A)

    ans = []

    maxA = max(A)
    AA = [a for a in A if a != maxA]
    if len(AA) == 0:
        ans.append(maxA)
    else:
        if len(AA) % 2 == 0:
            X = set(a1 + a2 for a1, a2 in zip(AA, AA[::-1]))
            if len(X) == 1 and X.pop() == maxA:
                ans.append(maxA)

    if len(A) % 2 == 0:
        X = set(a1 + a2 for a1, a2 in zip(A, A[::-1]))
        if len(X) == 1:
            ans.append(X.pop())

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(*ans)


if __name__ == "__main__":
    main()
