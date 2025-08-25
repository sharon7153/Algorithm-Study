import sys; sys.stdin = open('1225_genPWD.txt')

from collections import deque

T = 10

for _ in range(1, T+1):
    t = int(input())
    arr = list(map(int,input().split()))
    q = deque(arr)
    count = 1
    
    while 1:
        temp = q.popleft()
        temp -= count
        if temp <= 0:
            q.append(0)
            break
        q.append(temp)
        count = (count % 5) + 1
        
    print(f'#{t}', end = " ")
    print(*q)