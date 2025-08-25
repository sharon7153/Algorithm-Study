import sys; sys.stdin = open('5105_mazeDistance.txt')

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

### BFS 방식으로 최단 거리 찾기 ###
def bfs(s_i, s_j):
    visitied = [[-1]*(N) for _ in range(N)]  
    visitied[s_i][s_j] += 1
    q = deque()
    q.append([s_i, s_j])
    
    while q:
        ti, tj = q.popleft()
        if arr[ti][tj] == '3':
            return visitied[ti][tj] - 1
        
        for n in range(4):
            ni, nj = ti + di[n], tj + dj[n]
            
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and visitied[ni][nj] == -1:
                q.append([ni, nj])
                visitied[ni][nj] = visitied[ti][tj] + 1
     
    return 0


### DFS 방식으로 최단 거리 찾기 ###
# def dfs(s_i, s_j, dist):
#     global min_dist
#     if arr[s_i][s_j] == '3':
#         min_dist = min(min_dist, dist)        
#         return 
    
#     visitied[s_i][s_j] = 1
    
#     for n in range(4):
#         ni, nj = ni, nj = s_i + di[n], s_j + dj[n]
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and visitied[ni][nj] == 0:
#             dfs(ni, nj, dist+1)

#     visitied[s_i][s_j] = 0
    
    
    
## DFS 방식으로 도착 지점 존재 여부 확인 (재귀) ###
# def dfs_recur(s_i, s_j, visitied):
#     if arr[s_i][s_j] == '3':
#         return 1

#     visitied[s_i][s_j] = 1
    
#     for n in range(4):
#         ni, nj = ni, nj = s_i + di[n], s_j + dj[n]
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and visitied[ni][nj] == 0:
#             if dfs_recur(ni, nj, visitied):
#                 return 1
#     return 0


## DFS 방식으로 도착 지점 존재 여부 확인 (Stack) ###
# def dfs_stack(s_i, s_j, visitied):
#     stack = []
#     stack.append([s_i, s_j])
#     visitied[s_i][s_j] = 1

#     while 1:
        
#         if len(stack) == 0:
#             break
        
#         ti, tj = stack.pop()
#         if arr[ti][tj] == '3':
#             return 1


#         for n in range(4):
#             ni, nj = ni, nj = ti + di[n], tj + dj[n]
#             if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and visitied[ni][nj] == 0:
#                 stack.append([ni, nj])
#                 visitied[ni][nj] = 1
        
#     return 0        

    
T = int(input())

for t in range(1, T+1):

    N = int(input())
    arr = [input() for _ in range(N)]

    start_i_idx = 0
    start_j_idx = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_i_idx, start_j_idx = i, j
                break  

    visitied = [[0]*N for _ in range(N)] 
    
    
    ### BFS 방식으로 최단 거리 찾기 ###
    result_bfs = bfs(start_i_idx, start_j_idx)
    print(f'#{t} {result_bfs}')
    
    
    ### DFS 방식으로 최단 거리 찾기 ###
    # min_dist = float('inf')
    # dfs(start_i_idx, start_j_idx, 0)
    # result_dfs = 0
    # if min_dist != float('inf'):
    #     result_dfs = min_dist - 1
    # print(f'#{t} {result_dfs}') 
    
    
    ## DFS 방식으로 도착 지점 존재 여부 확인 (재귀) ###
    # result_dfs_recur = dfs_recur(start_i_idx, start_j_idx, visitied)
    # print(f'#{t} {result_dfs_recur}') 
    
    
    ## DFS 방식으로 도착 지점 존재 여부 확인 (Stack) ###
    # result_dfs_stack = dfs_stack(start_i_idx, start_j_idx, visitied)
    # print(f'#{t} {result_dfs_stack}') 
    
