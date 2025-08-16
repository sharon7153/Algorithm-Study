
### Stack 2개 이용한 방식 ####

# import sys; sys.stdin = open('2005_pascal.txt')

# T = int(input())

# for t in range(1, T+1):
#     N = int(input())
#     print(f'#{t}')
#     # stack 초기화 상태
#     stack = [1]

#     for _ in range(N):

#         # stack에 있는 값들 출력
#         for ele in stack:
#             print(ele, end = " ")
#         print()

#         # 파스칼 계산 위해 left 와 right 사용하여 계산
#         left = [0]
#         left.extend(stack)
#         right = stack[:]
#         right.extend([0])
        
#         # 새로운 리스트에 결과 값을 저장
#         new_stack = []
#         while 1:
#             if len(left) == 0 and len(right) == 0:
#                 break
#             new_stack.append(left.pop(0) + right.pop(0))
#         # 기존 리스트를 새로운 리스트로 변경 
#         stack = new_stack


### Stack 1개 이용한 방식 ####
import sys
sys.stdin = open('2005_pascal.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    print(f'#{t}')

    stack = [1]

    for _ in range(N):
        # 출력
        print(*stack)

        # 뒤에서 앞으로 업데이트
        stack.append(0)          # 마지막에 0 하나 추가
        print(stack)
        for i in range(len(stack)-1, 0, -1):
            stack[i] = stack[i] + stack[i-1]

