
answer = []
while 1:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    sides = sorted([a,b,c])
 
    if sides[0]**2 + sides[1]**2 == sides[2] ** 2:
        answer.append('right')
    else:
        answer.append('wrong')   

for result in answer:
    print(result)