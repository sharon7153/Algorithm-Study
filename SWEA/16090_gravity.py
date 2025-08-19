import sys; sys.stdin = open('16090_gravity.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())

    arr = list(map(int,input().split()))

    max_count = 0
    for i in range(N-1):
        count = 0
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                count += 1
        if max_count < count:
            max_count = count

    print(f'#{t} {max_count}')