import sys; sys.stdin = open('23795_spaceMonster.txt')


T = int(input())

for t in range(1, T+1):

    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    j_idx = 0
    i_idx = 0
    count_0 = 0

    for j in range(N):
        for i in range(N):
            if arr[j][i] == 2: # 괴물(2) 찾기
                j_idx = j
                i_idx = i
            if arr[j][i] == 0: # 빈칸(0) 세기
                count_0 += 1

    # 위, 오른쪽, 아래, 왼쪽
    dj = [-1, 0, 1, 0]
    di = [0, 1, 0, -1]

    # 괴물의 광선이 닿은 곳의 개수 세기
    count = 0
    for dir in range(4):
        nj = j_idx + dj[dir]
        ni = i_idx + di[dir]
        
        while 1:
            if nj < 0 or nj >= N or ni < 0 or ni >= N:
                break
            if arr[nj][ni] == 1:
                break
            if arr[nj][ni] == 0:
                count += 1
            
            nj = nj + dj[dir]
            ni = ni + di[dir]

    result = count_0 - count
    print(f'#{t} {result}')



    