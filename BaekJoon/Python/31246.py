
N, K = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# x = 0
# while True:
#     count = 0  
#     for a, b in zip(A, B):
#         if a + x >= b:
#             count += 1

#     if count >= K:
#         break
#     x += 1

## Method 1 ### (!! Time Out Issue !!!)
count = 0
i = 0
x = 0
while 1:
    if A[i%N] + x >= B[i%N]:
        count += 1
    else:
        pass
    
    if count == K:
        break
    i += 1
    
    if (i > N-1) and (i%N == 0):
        count = 0
        x += 1

print(x)