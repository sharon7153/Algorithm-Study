import sys; sys.stdin = open('5099_pizza.txt')

from collections import deque

T = int(input())

for t in range(1, T+1):

    N, M = map(int,input().split())
    cheese = list(map(int,input().split()))
    pizza = []
    for i in range(M):
        pizza.append([i+1, cheese[i]])

    on_pizza = deque()
    off_pizza = deque()

    for i in range(M):
        if i < N:
            on_pizza.append(pizza[i])
        else:
            off_pizza.append(pizza[i])

    while 1:
        if len(on_pizza) == 1:
            break
        
        temp = on_pizza.popleft()
        temp[1] = temp[1] // 2
        if temp[1] == 0:
            if len(off_pizza) != 0:
                on_pizza.append(off_pizza.popleft())
        else:
            # temp[1] = temp[1] // 2
            on_pizza.append(temp)

    print(f'#{t} {on_pizza[0][0]}')
    