def solve(N, A):
    imos = [0] * 1000000
    for a in A:
        imos[0] += 1
        imos[a] -= 1

    X = []
    x = 0
    for dx in imos:
        x += dx
        X.append(x)

    Y = []
    carry = 0
    for x in X:
        x += carry
        Y.append(x % 10)
        carry = x // 10
    while carry > 0:
        Y.append(carry % 10)
        carry //= 10

    ans = "".join(str(y) for y in Y[::-1])
    ans = ans.lstrip("0")

    return ans


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    main()
