w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())


# TR, TL, BL, TL
dq = [1, 1, -1, 1]
dp = [1, -1, -1, -1]

dir = 0
check = 0
count = 0
x = 0
y = 0
while 1:
    if check == t:
        y = q
        x = p
        break
    
    nq = q + dq[dir]
    np = p + dp[dir]
    
    if nq < 0 or nq > h or np < 0 or np > w:
        count += 1
        dir = count % 4
        nq = q + dq[dir]
        np = p + dp[dir]
    
    if nq == 0 or nq == h or np == 0 or np == w:
        count += 1
        dir = count % 4

    q = nq
    p = np
    
    check += 1

print(x,y)
    
    
    