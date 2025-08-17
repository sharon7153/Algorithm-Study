import sys; sys.stdin = open('4615_ocelloGame.txt')

T = int(input())

for t in range(1, T+1):
    
    N, M = map(int,input().split())

    board = [[0]*N for _ in range(N)]

    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2

    # TT, TR, RR, BR, BB, BL, LL, TL
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(M):
        x, y, color = map(int,input().split())
        y_idx, x_idx = y-1, x-1
        board[y_idx][x_idx] = color
        
        temp = []
        for dir in range(8):
            ny = y_idx + dy[dir]
            nx = x_idx + dx[dir]
            while 1:    
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    temp = []
                    break
                if board[ny][nx] == 0:
                    temp = []
                    break
                
                if color == 1:  # 흑돌인 경우
                    if board[ny][nx] == 2:
                        temp.append((ny,nx))
                        ny = ny + dy[dir]
                        nx = nx + dx[dir]
                    elif board[ny][nx] == 1:
                        while len(temp) != 0:
                            temp_y, temp_x = temp.pop()
                            board[temp_y][temp_x] = 1
                        break
                
                if color == 2:  # 백돌인 경우
                    if board[ny][nx] == 1:
                        temp.append((ny,nx))
                        ny = ny + dy[dir]
                        nx = nx + dx[dir]
                    elif board[ny][nx] == 2:
                        while len(temp) != 0:
                            temp_y, temp_x = temp.pop()
                            board[temp_y][temp_x] = 2
                        break

    count_black = 0
    count_white = 0
    for j in range(N):
        for i in range(N):
            if board[j][i] == 2:
                count_white += 1
            elif board[j][i] == 1:
                count_black += 1
                                
    print(f'#{t} {count_black} {count_white}')
