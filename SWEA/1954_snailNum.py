import sys; sys.stdin = open('1954_snailNum.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # R, B, L, T
    dj = [0, 1, 0, -1]
    di = [1, 0, -1, 0]

    j = 0
    i = 0
    dir = 0
    num = 1
    count = 0
    while 1:
        arr[j][i] = num
        
        if num == N*N:
            break
        
        nj = j + dj[dir]
        ni = i + di[dir]
        
        if nj < 0 or nj >= N or ni < 0 or ni >= N or arr[nj][ni] != 0:
            count += 1
            dir = count % 4
            nj = j + dj[dir]
            ni = i + di[dir]
        
        j = nj
        i = ni
        num += 1

    print(f'#{t}')
    for j in range(N):
        for i in range(N):
            print(arr[j][i], end =" ")
        print()