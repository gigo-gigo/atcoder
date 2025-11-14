class RollingHash:
    """Rolling Hash."""

    def __init__(
        self,
        S: str,
        BASE: int = 10007,
        MOD: int = 1000000007,
    ) -> None:
        """Preprocessing for rolling hash.

        Args:
            S (str): String.
            BASE (int, optional): Base number. Defaults to 10007.
            MOD (int, optional): Prime. Defaults to 1000000007.
        """
        self.S = S
        self.N = len(S)
        self.BASE = BASE
        self.MOD = MOD

        self.AA = [0]
        for s in self.S:
            c = ord(s)
            aa = self.AA[-1] * self.BASE + c
            aa %= self.MOD
            self.AA.append(aa)

        self.B = [1]
        for _ in self.S:
            b = self.B[-1] * self.BASE
            b %= self.MOD
            self.B.append(b)

    def query(self, left: int, right: int) -> int:
        """Hash for S[left:right] (left inclusive, right exclusive).

        Args:
            left (int): [0, N]
            right (int): [left, N], right >= left

        Returns:
            int: Hash.
        """
        h = self.AA[right] - self.B[right - left] * self.AA[left]
        h %= self.MOD

        return h


def solve(S, T):
    rhS = RollingHash(S)
    rhT = RollingHash(T)
    N = len(S)
    for i in range(N + 1):
        if rhS.query(0, i) == rhT.query(N - i, N) and rhS.query(i, N) == rhT.query(
            0, N - i
        ):
            return i

    return -1


def main():
    T = int(input())
    ans = []
    for _ in range(T):
        S = input()
        T = input()
        x = solve(S, T)
        ans.append(x)
    print(*ans)


if __name__ == "__main__":
    main()
