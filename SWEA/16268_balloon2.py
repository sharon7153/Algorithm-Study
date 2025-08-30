import sys; sys.stdin = open('16268_balloon2.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_sum = 0

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N):
        for j in range(M):
            temp_sum = arr[i][j]
            for n in range(4):
                ni, nj = i + di[n], j + dj[n]
                
                if 0 <= ni < N and 0 <= nj < M:
                    temp_sum += arr[ni][nj]
            if max_sum < temp_sum:
                max_sum = temp_sum

    print(f'#{t} {max_sum}')
        