import sys; sys.stdin = open('4751_diamond.txt')

def makeDiamond(ch):
    arr = [['.']* 5 for _ in range(5)]
    for row in range(5):
        if row == 0 or row == 4:
            arr[row][2] = '#'
        elif row == 1 or row == 3:
            arr[row][1] = '#'
            arr[row][3] = '#'
        else:
            arr[row][0] = '#'
            arr[row][4] = '#'
            arr[row][2] = ch
    return arr
            

T = int(input())

for t in range(1, T+1):

    string = input()

    ### 풀이 1 ###
    diamond_str = []
    for idx, ch in enumerate(string):
        diamond_ch = makeDiamond(ch)
        if idx == 0:
            for i in range(5):
                diamond_str.append(diamond_ch[i])
                
        else:
            for i in range(5):
                diamond_str[i] = diamond_str[i][:-1] + diamond_ch[i]
    for i in range(5):
        print(''.join(diamond_str[i]))

    ### 풀이 2 (틀림) ###
    # if len(string) == 1:
    #     diamond_ch = makeDiamond(string)
    #     for i in range(5):
    #         print(''.join(diamond_ch[i]))
    # else:
    #     diamond_str = []
    #     for ch in string:
    #         diamond_ch = makeDiamond(ch)
    #         if ch == string[0]:
    #             for i in range(5):
    #                 diamond_str.append(diamond_ch[i][:-1])
    #         elif ch == string[-1]:
    #             for i in range(5):
    #                 diamond_str[i].extend(diamond_ch[i])
    #         else:
    #             for i in range(5):
    #                 diamond_str[i].extend(diamond_ch[i][:-1])
                 
    #     for i in range(5):
    #         print(''.join(diamond_str[i]))