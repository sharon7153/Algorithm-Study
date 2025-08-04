T = int(input())

N = [0]*T
K = [0]*T

for i in range(T):
    N[i], K[i] = map(int,input().split())


def cal_division(n):
    data = []
    for i in range(1,n+1):
        if n % i == 0:
            data.append(i)
    return data    


for i in range(T):
    n = N[i]
    k = K[i]
    
    count_k = 0
    while n > 0:
        arr = cal_division(n)
        # print(arr)
        count_even = 0
        count_odd = 0
        for ele in arr:
            if ele % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        # print(f'even : {count_even}, odd : {count_odd}')
        if k*count_odd == count_even:
            # print(f'MATCH!!! {count_even} = {k}*{count_odd}')
            count_k += 1 
        n -= 1
    print(count_k)