import sys; sys.stdin = open('1219_findPath.txt')

T = 10


for t in range(1, T+1):
    t, N = map(int,input().split())
    inputs = list(map(int,input().split()))
    
    node_arr = [[] for _ in range(100)]
    
    for i in range(0,len(inputs),2):
        node_arr[inputs[i]].append(inputs[i+1])

    visitied = [0]*100

    def dfs(start):
        
        if start == 99:
            return 1
        
        if visitied[start] == 1:
            return 0
        
        visitied[start] = 1
        
        for ele in node_arr[start]:
            # if visitied[ele] == 0:
            if dfs(ele):
                return 1
        
        return 0


    result = dfs(0)
    print(f'#{t} {result}')
    
        