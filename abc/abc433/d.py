from collections import Counter


def solve(N, M, A):
    Cs = [Counter()]
    for digit in range(1, 11):
        C = Counter()
        for a in A:
            r = (a % M) * pow(10, digit, M) % M
            C[r] += 1
        Cs.append(C)

    ans = 0
    for a in A:
        digit = len(str(a))
        r = (-(a % M)) % M
        ans += Cs[digit][r]

    return ans


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = solve(N, M, A)
    print(ans)


if __name__ == "__main__":
    main()
