import sys
input = sys.stdin.readline


def count_win(A, B, x):
    return sum(1 for a, b in zip(A,B) if a + x >= b)

N, K = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

left = 0
right = 10**9
answer = -1

while left <= right:
    mid = (left + right) // 2
    if count_win(A, B, mid) >= K:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
    