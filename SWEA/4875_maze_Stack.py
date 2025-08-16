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

    visitied = [[0]*N for _ in range(N)]
    visitied[start_y_idx][start_x_idx] = 1

    # top, right, bottom, left
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    stack = [(start_y_idx, start_x_idx)]
    result = 0
    
    while 1:
        if len(stack) == 0:
            break
        
        y_idx, x_idx = stack.pop()

        for dir in range(4):
            ny = y_idx + dy[dir]
            nx = x_idx + dx[dir]
            
            # 범위를 벗어날 경우
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            
            # 벽이거나 이미 방문한 경우
            if arr[ny][nx] == '1' or visitied[ny][nx] == 1:
                continue
            
            # 도착점 일 경우
            if arr[ny][nx] == '3':
                result = 1
                stack = []
                break
            
            # 이동 가능한 경로
            if arr[ny][nx] == '0' and visitied[ny][nx] == 0:
                visitied[ny][nx] = 1
                stack.append((ny,nx))
                
    print(f'#{t} {result}')
    

    #### Stack 사용하지 않고 실수한 버전 ####
    # stack = []
    # y_idx = start_y_idx
    # x_idx = start_x_idx
    # result = 0
    
    # while 1:
    #     found = 0
    #     count = 0
    #     for dir in range(4):
    #         count += 1
    #         ny = y_idx + dy[dir]
    #         nx = x_idx + dx[dir]
            
    #         if ny < 0 or ny >= N or nx < 0 or nx >= N:
    #             continue
            
    #         if arr[ny][nx] == '1' or visitied[ny][nx] == 1:
    #             continue
            
    #         if arr[ny][nx] == '3':
    #             found = 1
    #             break
            
    #         if arr[ny][nx] == '0' and visitied[ny][nx] == 0:
    #             visitied[ny][nx] = 1
    #             y_idx = ny
    #             x_idx = nx
    #             break
            
    #     if found:
    #         result = 1
    #         break
    #     elif found == 0 and count == 4 and arr[ny][nx] != '0':
    #         y_idx = start_y_idx
    #         x_idx = start_x_idx



    # print(f'#{t} {result}')
    

