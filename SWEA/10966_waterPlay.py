import sys; sys.stdin = open('10966_waterPlay.txt')

from collections import deque
T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())

    arr = [input() for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i,j])
                visited[i][j] = 0

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    dist = 0
    while 1:
        if len(q) == 0:
            break
        
        ti, tj = q.popleft()
        
        for n in range(4):
            ni = ti + di[n]
            nj = tj + dj[n]
            
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1:
                q.append([ni,nj])
                visited[ni][nj] = visited[ti][tj] + 1
                dist += visited[ni][nj]

    print(f'#{t} {dist}')