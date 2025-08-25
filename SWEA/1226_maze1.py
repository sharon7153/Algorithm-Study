import sys; sys.stdin = open('1226_maze1.txt')

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def bfs(si, sj):
    visitied = [[0]*N for _ in range(N)]
    q = deque()
    q.append([si,sj])
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == '3':
            return 1
        for n in range(4):
            ni, nj = ti + di[n], tj + dj[n]
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visitied[ni][nj] == 0:
                visitied[ni][nj]= 1
                q.append([ni,nj])
    return 0

def dfs(si, sj):
    
    if si < 0 or si >= N or sj < 0 or sj >= N: 
        return 0
    if maze[si][sj] == '3':
        return 1
        
    visited_dfs[si][sj] = 1
    
    for n in range(4):
        ni, nj = si + di[n], sj + dj[n]
        if visited_dfs[ni][nj] == 0 and maze[ni][nj] != '1':
            if dfs(ni,nj):
                return 1
    
    return 0
    

T = 10

for _ in range(1, T+1):

    t = int(input())
    N = 16
    maze = [input() for _ in range(N)]

    st_i, st_j = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                st_i, st_j = i, j

    result = bfs(st_i, st_j)
    
    visited_dfs = [[0]*N for _ in range(N)]
    # result = dfs(st_i, st_j)

    print(f'#{t} {result}')