def solve(N, A):
    A = [0] + A
    i = 1
    right = 2
    while i <= N:
        X = []
        for j in range(right, min(N + 1, i + A[i])):
            X.append((j + A[j], j))
        if X:
            right = min(N + 1, i + A[i])
            _, i = max(X)
        else:
            break

    return right - 1


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
