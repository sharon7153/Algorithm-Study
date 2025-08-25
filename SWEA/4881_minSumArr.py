import sys; sys.stdin = open('4881_minSumArr.txt')

def f(i, N, s):
    global min_value 
    
    if i == N:
        if min_value > s:
            min_value = s
    elif min_value < s:
        return
    else:    
        for j in range(i,N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    p = [i for i in range(N)]
    min_value = 10000

    f(0, N, 0)

    print(f'#{t} {min_value}')

