N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

heights = [0]*1001

for x,h in arr:
    heights[x] = h

max_h = max(heights)
max_idx = heights.index(max_h)

area = 0
current_height = 0
for i in range(0, max_idx +1):
    if heights[i] > current_height:
        current_height = heights[i]
    area += current_height

current_height = 0
for i in range(1000, max_idx, -1):
    if heights[i] > current_height:
        current_height = heights[i]
    area += current_height

print(area)