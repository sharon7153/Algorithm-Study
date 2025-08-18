import sys; sys.stdin = open('1248_commonAncestor.txt')

T = int(input())

# for t in range(1, T+1):

V, E, node_1, node_2 = map(int,input().split())

inputs = list(map(int,input().split()))
node_arr = [[] for _ in range(V+1)]

for i in range(0,len(inputs),2):
    n = inputs[i]
    node_arr[n].append(inputs[i+1])

# print(node_arr)

