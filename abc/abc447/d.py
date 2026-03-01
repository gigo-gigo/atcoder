from sortedcontainers import SortedList


def solve(S):
    sla = SortedList()
    slc = SortedList()
    for m, s in enumerate(S):
        if s == "A":
            sla.add(m)
        elif s == "C":
            slc.add(m)

    ans = 0
    for j, s in enumerate(S):
        if s != "B":
            continue
        ii = sla.bisect_left(j) - 1
        i = sla[ii] if ii >= 0 else -1
        kk = slc.bisect_left(j)
        k = slc[kk] if kk < len(slc) else -1
        if 0 <= i < j < k:
            sla.remove(i)
            slc.remove(k)
            ans += 1

    return ans


def main():
    S = input()
    ans = solve(S)
    print(ans)


if __name__ == "__main__":
    main()
