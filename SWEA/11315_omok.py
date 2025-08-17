import sys; sys.stdin = open('11315_omok.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())
    board = [input() for _ in range(N)]

    # R, BR, B, BL
    dj = [0, 1, 1, 1]
    di = [1, 1, 0, -1]

    found = 0
    for j in range(N):
        for i in range(N):
            if board[j][i] == 'o':
                count = 1
                for dir in range(4):
                    nj = j + dj[dir]
                    ni = i + di[dir]
                    
                    while 1:
                        if nj < 0 or nj >= N or ni < 0 or ni >= N:
                            count = 1
                            break
                        
                        if board[nj][ni] == 'o':
                            count += 1
                            nj = nj + dj[dir]
                            ni = ni + di[dir]
                        else: 
                            count = 1
                            break
                        if count >=5 :
                            found = 1
                            break
                    if found == 1:
                        break
            if found == 1:
                break
        if found == 1:
                break

    if found == 1:
        result = 'YES'
    else:
        result = 'NO'

    print(f'#{t} {result}') 
                