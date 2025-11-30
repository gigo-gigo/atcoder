class CumSum2D:
    """Cumulative sum for 2D list."""

    def __init__(self, A: list[list[int]]) -> None:
        self.A = A
        self.H = len(A)
        self.W = len(A[0])
        self.accA = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        for h in range(self.H):
            for w in range(self.W):
                value = (
                    A[h][w]
                    + self.accA[h + 1][w]
                    + self.accA[h][w + 1]
                    - self.accA[h][w]
                )
                self.accA[h + 1][w + 1] = value

    def query(self, h1: int, w1: int, h2: int, w2: int) -> int:
        """Return the cumulative sum for h1 <= h < h2 and w1 <= w < w2.

        Args:
            h1 (int): [0, H]
            h2 (int): [h1, H]
            w1 (int): [0, W]
            w2 (int): [w1, W]

        Returns:
            int: cumulative sum.
        """
        value = (
            self.accA[h2][w2]
            - self.accA[h2][w1]
            - self.accA[h1][w2]
            + self.accA[h1][w1]
        )

        return value


def solve(N, ABCD, MAX=2000):
    A = [[0] * (MAX + 1) for _ in range(MAX + 1)]
    for a, b, c, d in ABCD:
        A[a][b] += 1
        A[a][d] -= 1
        A[c][b] -= 1
        A[c][d] += 1
    X = CumSum2D(A)

    B = [[0] * MAX for _ in range(MAX)]
    for row in range(MAX):
        for column in range(MAX):
            B[row][column] = int(X.query(0, 0, row + 1, column + 1) > 1)
    Y = CumSum2D(B)

    cloud_area = 0
    for row in range(MAX):
        for column in range(MAX):
            cloud_area += int(X.query(0, 0, row + 1, column + 1) > 0)

    ans = []
    for a, b, c, d in ABCD:
        unique_area = (c - a) * (d - b) - Y.query(a, b, c, d)
        ans.append(MAX * MAX - (cloud_area - unique_area))

    return ans


def main():
    N = int(input())
    ABCD = []
    for _ in range(N):
        a, c, b, d = map(int, input().split())
        a -= 1
        b -= 1
        ABCD.append((a, b, c, d))
    ans = solve(N, ABCD)
    print(*ans)


if __name__ == "__main__":
    main()
