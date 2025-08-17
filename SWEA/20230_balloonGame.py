import sys; sys.stdin = open('20230_balloonGame.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    row = [0]*N
    col = [0]*N

    for j in range(N):
        for i in range(N):
            row[j] += arr[j][i]
            col[j] += arr[i][j]

    max_total = 0
    total = 0
    for j in range(N):
        for i in range(N):
            total += row[j]
            total += col[i]
            total -= arr[j][i]
            if max_total < total:
                max_total = total
            total = 0

    print(f'#{t} {max_total}')
    