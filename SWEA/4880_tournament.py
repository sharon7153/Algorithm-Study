import sys; sys.stdin = open('4880_tournament.txt')

# 1 : 가위, 2: 바위, 3: 보
def compete(left, right):
    l_no, r_no = left[0], right[0]
    l_card, r_card = left[1], right[1]
    if l_card == r_card:
        if l_no < r_no: 
            return left
        else: 
            return right
    elif (l_card == 1 and r_card == 3) or (l_card == 2 and r_card == 1) or (l_card == 3 and r_card == 2):
        return left
    else:
        return right 
            
#### 문제가 있는 winner 함수 ####
# def winner(sets):
#     n = len(sets)
#     left = sets[:n//2]
#     right = sets[n//2:]
    
#     if len(left) == 1 and len(right) == 1:
#         # return compete(left[0], right[0])
#         return sets[0]
    
#     left_winner = winner(left)
#     right_winner = winner(right)
    
#     return compete(left_winner, right_winner)

#### 재귀 방법 1 ####
# def winner(sets, s_idx, e_idx):
#     if s_idx == e_idx:
#         return sets[s_idx]
    
#     mid_idx = (s_idx + e_idx) // 2
#     left_winner = winner(sets, s_idx, mid_idx)
#     right_winner = winner(sets, mid_idx + 1, e_idx)
    
#     return compete(left_winner,right_winner)
    
#### 재귀 방법 2 ####
def winner(sets):
    if len(sets) == 1:
        return sets[0]
    
    mid = len(sets) // 2
    left_winner = winner(sets[:mid])
    right_winner = winner(sets[mid:])
    
    return compete(left_winner,right_winner)

T = int(input())

for t in range(1, T+1):

    N = int(input())

    cards = list(map(int,input().split()))
    sets = []

    for i in range(N):
        sets.append((i+1,cards[i]))

    # final_winner = winner(sets, 0, N-1)
    final_winner = winner(sets)

    # print(f'#{final_winner[0]}')
    print(f'#{t} {final_winner[0]}')