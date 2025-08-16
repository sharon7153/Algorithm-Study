import sys; sys.stdin = open('22375_switchControl.txt')

T = int(input())

for t in range(1, T+1):

    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    count = 0
    for i in range(N):
        if A[i] != B[i]:
            count += 1
            for j in range(i,N):
                A[j] = 1 - A[j]

    print(f'#{t} {count}')