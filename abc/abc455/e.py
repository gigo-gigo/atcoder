from collections import Counter


def solve(N, S):
    A = [0]
    B = [0]
    C = [0]
    for s in S:
        A.append(A[-1] + int(s == "A"))
        B.append(B[-1] + int(s == "B"))
        C.append(C[-1] + int(s == "C"))

    ans = N * (N + 1) // 2

    X = Counter()
    for a, b, c in zip(A, B, C):
        X[(a - b, a - c)] += 1
    for v in X.values():
        ans += 2 * (v * (v - 1) // 2)

    X = Counter()
    for a, b in zip(A, B):
        X[a - b] += 1
    for v in X.values():
        ans -= v * (v - 1) // 2

    X = Counter()
    for a, c in zip(A, C):
        X[a - c] += 1
    for v in X.values():
        ans -= v * (v - 1) // 2

    X = Counter()
    for b, c in zip(B, C):
        X[b - c] += 1
    for v in X.values():
        ans -= v * (v - 1) // 2

    return ans


def main():
    N = int(input())
    S = input()
    ans = solve(N, S)
    print(ans)


if __name__ == "__main__":
    main()
