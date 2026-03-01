from more_itertools import run_length


def preprocess(S):
    X = []
    x = 0
    for s in S:
        if s == "A":
            x += 1
        else:
            X.append(x)
            x = 0
    X.append(x)

    return X


def solve(S, T):
    if S.replace("A", "") != T.replace("A", ""):
        return -1

    ans = 0
    for x, y in zip(preprocess(S), preprocess(T)):
        ans += abs(x - y)

    return ans


def main():
    S = input()
    T = input()
    ans = solve(S, T)
    print(ans)


if __name__ == "__main__":
    main()
