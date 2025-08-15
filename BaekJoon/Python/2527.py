
result = ''
result_arr = []
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())

    overlap_x = min(p1, p2) - max(x1, x2)
    overlap_y = min(q1, q2) - max(y1, y2)
    
    if overlap_x < 0 or overlap_y < 0:
        result = 'd'
    elif overlap_x > 0 and overlap_y > 0:
        result = 'a'
    elif overlap_x == 0 and overlap_y == 0:
        result = 'c'
    elif overlap_x == 0 and overlap_y > 0:
        result = 'b'
    elif overlap_x > 0 and overlap_y == 0:
        result = 'b'
    result_arr.append(result)

for i in result_arr:        
    print(i)