class Node:
    def __init__(self, x):
        self.x = x
        self.prev = None
        self.next = None

    def add_next(self, other):
        if other.prev:
            other.prev.next = None
            other.prev = None
        self.next = other
        other.prev = self

    def count(self):
        c = 0
        other = self
        while other is not None:
            c += 1
            other = other.next

        return c

    def __repr__(self):
        return f"Node({self.x}, prev={self.prev.x if self.prev else None}, next={self.next.x if self.next else None})"


def solve(N, queries):
    A = [Node(i) for i in range(N + 1)]
    for c, p in queries:
        node1 = A[c]
        node2 = A[p]
        node2.add_next(node1)

    X = [0] * (N + 1)
    for i, node in enumerate(A):
        if node.prev is None:
            X[i] = node.count()

    return X[1:]


def main():
    N, Q = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        c, p = list(map(int, input().split()))
        queries.append((c, p))
    ans = solve(N, queries)
    print(*ans)


if __name__ == "__main__":
    main()
