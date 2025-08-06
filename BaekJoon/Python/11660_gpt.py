import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N + 1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

# 누적합 배열
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

# 누적합 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = (
            arr[i][j]
            + prefix_sum[i - 1][j]
            + prefix_sum[i][j - 1]
            - prefix_sum[i - 1][j - 1]
        )

# 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    total = (
        prefix_sum[x2][y2]
        - prefix_sum[x1 - 1][y2]
        - prefix_sum[x2][y1 - 1]
        + prefix_sum[x1 - 1][y1 - 1]
    )
    print(total)
