import sys; sys.stdin = open('5097_rotation.txt')

from collections import deque
T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    q = deque(arr)

    for _ in range(M):
        temp = q.popleft()
        q.append(temp)

    print(f'#{t} {q[0]}')
