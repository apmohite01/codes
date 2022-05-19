from collections import deque


def bfs(graph,root):

    # queue banvli 
    queue=deque()
    # visited mark krnya sathi set banvla
    vis=set()

    # 0 la queue ani set mdhe tkla
    queue.append(root)
    vis.add(root)

    while(queue): # jo prynt queue  empty ny hot
        vertex=queue.popleft()   #queue cha first elem pop krnar
        print(vertex ,end=" ")   
        # o che sagle neighbour iterate krycha
        for x in graph[vertex]:
            if x not in vis:
                queue.append(x)
                vis.add(x)

graph= { 0:[1,2] ,1:[3,4],2:[5,6],3:[8],4:[],5:[7],6:[],7:[],8:[]}

bfs(graph,0)



#--------------------------------------------------------------
print("\n\n----------------------------")
visited=set()


def dfs(graph,visited,root):

    print(root,end=" ")
    visited.add(root)

    for x in graph[root]:
        if x not in visited:
            dfs(graph,visited,x)
dfs(graph,visited,0)