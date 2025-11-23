def solve(queries):
    ans = []
    lifo = []
    x = 0
    is_good = True

    for q, c in queries:
        if q == 1:
            dx = 1 if c == "(" else -1
            if is_good and x == 0 and dx == -1:
                is_good = False
                lifo.append((c, True))
            else:
                lifo.append((c, False))
            x += dx
        else:
            c, f = lifo.pop()
            if c == "(":
                x -= 1
            else:
                x += 1
            if f:
                is_good = True

        if is_good and x == 0:
            ans.append("Yes")
        else:
            ans.append("No")

    return ans


def main():
    Q = int(input())
    queries = []
    for _ in range(Q):
        S = input()
        q, c = int(S[0]), S[-1]
        queries.append((q, c))
    ans = solve(queries)
    print(*ans)


if __name__ == "__main__":
    main()
