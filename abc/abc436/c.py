def solve(RC):
    blocks = set()
    ans = 0
    for r, c in RC:
        if (
            (r, c) in blocks
            or (r, c + 1) in blocks
            or (r + 1, c) in blocks
            or (r + 1, c + 1) in blocks
        ):
            continue
        blocks.add((r, c))
        blocks.add((r, c + 1))
        blocks.add((r + 1, c))
        blocks.add((r + 1, c + 1))
        ans += 1

    return ans


def main():
    N, M = map(int, input().split())
    RC = []
    for _ in range(M):
        r, c = map(int, input().split())
        RC.append((r, c))
    ans = solve(RC)
    print(ans)


if __name__ == "__main__":
    main()
