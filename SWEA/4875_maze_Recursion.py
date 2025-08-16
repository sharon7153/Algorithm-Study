import sys; sys.stdin = open('4875_maze.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())

    arr = [input() for _ in range(N)]

    start_y_idx = 0
    start_x_idx = 0
    for j in range(N):
        for i in range(N):
            if arr[j][i] == '2':
                start_y_idx = j
                start_x_idx = i

    # print(start_y_idx, start_x_idx)
    visitied = [[0]*N for _ in range(N)]

    def dfs(y_idx, x_idx):
        
        if y_idx < 0 or y_idx >= N or x_idx < 0 or x_idx >= N:
            return 0
        
        if visitied[y_idx][x_idx] == 1 or arr[y_idx][x_idx] == '1':
            return 0
        
        if arr[y_idx][x_idx] == '3':
            return 1
        
        visitied[y_idx][x_idx] = 1
        
        if dfs(y_idx-1, x_idx) or dfs(y_idx, x_idx+1) or dfs(y_idx+1, x_idx) or dfs(y_idx, x_idx-1):
            return 1
        
        return 0

        
    result = dfs(start_y_idx, start_x_idx)

    print(f'#{t} {result}')