"""
In this game, PacMan is positioned in a grid. PacMan has to find the food using Breadth First Search (BFS), provided the grid is completely observable, perform a BFS on the grid and then print the path obtained by BFS from the PacMan to the food.
"""

from collections import deque 
import copy

p = tuple(map(int, input().split()))
f = tuple(map(int, input().split()))
N , M = list(map(int, input().split()))
grid = []
explored_nodes = []
aux = deque()
res = None

rt = []

for i in range(0, N):
    grid.append(list(map(str, input())))

#U L R D
directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

aux.append([p[0], p[1], []])
while len(aux) > 0:
    x, y, r = aux.popleft()
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