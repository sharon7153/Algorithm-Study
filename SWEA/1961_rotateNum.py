import sys; sys.stdin = open('1961_rotateNum.txt')

T = int(input())

for t in range(1, T+1):
    def rotate(arr):
        n = len(arr)
        new_arr = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(n):
                new_arr[j][i] = arr[n-1-i][j]
        return new_arr
                

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rotate_90 = rotate(arr)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    print(f'#{t}')
    for j in range(N):
        for i in range(N):
            print(rotate_90[j][i],end="")
        print(end=" ")
        for i in range(N):
            print(rotate_180[j][i],end="")
        print(end=" ")
        for i in range(N):
            print(rotate_270[j][i],end="")
        print()
