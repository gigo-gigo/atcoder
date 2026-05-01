def simplify(S):
    lifo = []
    p = False
    x = 0
    for s in S:
        if s == "(":
            lifo.append(s)
            p = True
            x = 0
        elif s == ")":
            lifo.append(s)
            if p and x == 2:
                lifo.pop()
                lifo.pop()
                lifo.pop()
                lifo.pop()
                lifo.append("x")
                lifo.append("x")
            if (
                len(lifo) >= 3
                and lifo[-3] == "("
                and lifo[-2] == "x"
                and lifo[-1] == "x"
            ):
                pass
            else:
                p = False
                x = 0
        elif s == "x":
            lifo.append(s)
            x += 1
        else:
            raise ValueError("invalid char")

    T = "".join(lifo)

    return T


def solve(A, B):
    AA = simplify(A)
    BB = simplify(B)
    # print(f"{A=}, {AA=}, {B=}, {BB=}")

    return AA == BB


def main():
    T = int(input())
    X = []
    for _ in range(T):
        A = input()
        B = input()
        x = "Yes" if solve(A, B) else "No"
        X.append(x)
    print(*X)


if __name__ == "__main__":
    main()
