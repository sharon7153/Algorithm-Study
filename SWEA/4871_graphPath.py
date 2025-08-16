import sys
sys.stdin = open('4871_graphPath.txt')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())

    node_arr =[[] for _ in range(V+1)]
    # print(node_arr)

    for _ in range(E):
        start_node, end_node = map(int, input().split())
        node_arr[start_node].append(end_node)

    S, G = map(int,input().split())
    # print(node_arr)    

    visitied = [0]*(V+1)

    def dfs(s):
        if s == G:
            return 1
        
        visitied[s] = 1
        
        
        for i in node_arr[s]:
            if visitied[i] == 0:
                if dfs(i) == 1:
                    return 1
            
        return 0

    result = dfs(S)

    print(f'#{t} {result}')