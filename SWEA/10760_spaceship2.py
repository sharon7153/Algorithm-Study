import sys; sys.stdin = open('10760_spaceship2.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    result = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for n in range(8):
                ni, nj = i + di[n], j + dj[n]
                    
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[i][j] > arr[ni][nj]:
                        count += 1
            
            if count >= 4:
                result += 1

    print(f'#{t} {result}')  
