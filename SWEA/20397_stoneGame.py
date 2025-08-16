import sys; sys.stdin = open('20397_stoneGame.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    arr = list(map(int,input().split()))

    for _ in range(M):  
        i, j = map(int, input().split())
        i_idx = i -1
        for n in range(1,j+1):
            if i_idx-n >= 0 and i_idx+n < N:    
                if arr[i_idx-n] == arr[i_idx+n]:
                    arr[i_idx-n] = 1 - arr[i_idx-n]
                    arr[i_idx+n] = 1 - arr[i_idx+n]

    print(f'#{t}', end=" ")
    print(*arr)
