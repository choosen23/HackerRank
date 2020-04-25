"""
In this game, PacMan is positioned in a grid. PacMan has to find the food using Depth First Search (DFS). Assume the grid is completely observable, perform a DFS on the grid and then print the path obtained by DFS from the PacMan to the food.
"""








def adjacent(g,point):
    x , y = point[0] , point[1]
    res = []
    #D R L U
    for i in (x+1,y) , (x,y+1) , (x,y-1) , (x-1,y) :
        if g[i[0]][i[1]] in ['-','.']:
            res.append(i)
    # res.reverse()
    return res



import copy

p = tuple(map(int, input().split()))
f = tuple(map(int, input().split()))
N , M = list(map(int, input().split()))
grid = []
explored_nodes = []
aux = []
res = None

rt = []

for i in range(0, N):
    grid.append(list(map(str, input())))

#U L R D
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

aux.append([p[0], p[1], []])
while len(aux) > 0:
    x, y, r = aux.pop()
    routes = copy.deepcopy(r)
    routes.append([x, y])   

 

    explored_nodes.append([x, y])
    
    if (x,y) == f:
        if res == None:
            res = routes
            break

    for direction in directions:
        next_x, next_y = x + direction[0], y + direction[1]
        if next_x not in range(0,N) or next_y not in range(0,M):
            continue

        if grid[next_x][next_y] in ["-","."]:
            grid[next_x][next_y] = '='
            aux.append([next_x, next_y, routes])
            


print(str(len(explored_nodes)))
for point in explored_nodes:
    print(str(point[0]) + " " + str(point[1]))

print(str(len( res)  - 1))
for point in res:
    print(str(point[0]) + " " + str(point[1]))