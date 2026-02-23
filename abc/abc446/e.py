class SCCGraph:
    """AtCoder Library (ACL) 互換の強連結成分分解 (非再帰版)"""

    def __init__(self, n: int):
        self._n = n
        self._edges: list[tuple[int, int]] = []

    def add_edge(self, from_node: int, to_node: int) -> None:
        assert 0 <= from_node < self._n
        assert 0 <= to_node < self._n
        self._edges.append((from_node, to_node))

    def _build_adj(self) -> list[list[int]]:
        adj: list[list[int]] = [[] for _ in range(self._n)]
        for u, v in self._edges:
            adj[u].append(v)
        return adj

    def scc(self) -> list[list[int]]:
        adj = self._build_adj()

        index = [-1] * self._n

        lowlink = [0] * self._n
        stack: list[int] = []
        on_stack = [False] * self._n
        sccs: list[list[int]] = []
        cur_index = 0

        for v_start in range(self._n):
            if index[v_start] != -1:
                continue

            # call_stack: (vertex, next_edge_index)
            call_stack: list[tuple[int, int]] = [(v_start, 0)]
            while call_stack:
                v, ei = call_stack[-1]

                if ei == 0:
                    index[v] = lowlink[v] = cur_index
                    cur_index += 1
                    stack.append(v)
                    on_stack[v] = True

                if ei < len(adj[v]):
                    # explore next child
                    w = adj[v][ei]
                    call_stack[-1] = (v, ei + 1)
                    if index[w] == -1:
                        call_stack.append((w, 0))
                        continue
                    if on_stack[w]:
                        lowlink[v] = min(lowlink[v], index[w])
                    continue

                # finished all children of v
                if lowlink[v] == index[v]:
                    comp: list[int] = []
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp.append(w)
                        if w == v:
                            break
                    sccs.append(comp)

                call_stack.pop()
                if call_stack:
                    parent, _ = call_stack[-1]
                    lowlink[parent] = min(lowlink[parent], lowlink[v])

        return sccs[::-1]


def solve(m, a, b):
    A = [-1] * (m * m)
    for x in range(m):
        for y in range(m):
            u = y * m + x
            z = (a * y % m + b * x % m) % m
            v = z * m + y
            A[u] = v

    G = SCCGraph(m * m)
    for u, v in enumerate(A):
        G.add_edge(u, v)

    X = [False] * (m * m)
    for x in range(m):
        for y in range(m):
            u = y * m + x
            if x % m == 0 or y % m == 0:
                X[u] = True

    for group in G.scc()[::-1]:
        if len(group) > 1:
            if any(X[u] for u in group):
                for u in group:
                    X[u] = True
        else:
            u = group[0]
            v = A[u]
            X[u] |= X[v]

    ans = m * m - sum(X)

    return ans


def main():
    m, a, b = list(map(int, input().split()))
    ans = solve(m, a, b)
    print(ans)


if __name__ == "__main__":
    main()
