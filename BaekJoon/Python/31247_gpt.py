import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    res = []
    for _ in range(T):
        N, K = map(int,input().split())

        if K >= 64:
            res.append(0)
        else:
            denom = 1 << K
            if denom > N:
                res.append(0)
            else:
                m = N // denom
                count = (m + 1) // 2
                res.append(count)
      
    for i in res:
        print(i)

solve()
