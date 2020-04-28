
import sys

def adjacent(g,point):
    x , y = point[0] , point[1]
    res = []
    #D R L U
    for i in (x+1,y) , (x,y+1) , (x,y-1) , (x-1,y) :
        if g[i[0]][i[1]] in ['-','.']:
            res.append(i)
    return res


#manhattan distance between 2 points a and b
def manhattan_distance(a,b):
    return  abs(a[0] - b[0]) + abs(a[1] - b[1])

def findObstacles(grid):
    obst = []
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] == '%':
                obst.append((i,j))
    return set(obst)



#cost for every objsacle get extremly high
def move_cost(a, b ,barriers):
    if b in barriers:
            return sys.maxsize #Extremely high cost to enter barrier squares
    return 1 #Normal movement cost


def AStarSearch( graph,start, end,case):

    G = {} #Actual movement cost to each position from the start position
    F = {} #Estimated movement cost of start to end going via this position
    frontier = []
    expanded_nodes = []
    
    obstacles = findObstacles(grid)

    G[start] = 0 
    F[start] = manhattan_distance(start, end)
    closedVertices = set()
    openVertices = set([start])
    cameFrom = {}

    while len(openVertices) > 0:
        #Get the vertex in the open list with the lowest F score
        current = None
        currentFscore = None
        for pos in openVertices:
            if current is None or F[pos] < currentFscore:
                currentFscore = F[pos]
                current = pos

        #Check if we have reached the goal
        if current == end:
            #Retrace our route backward
            openVertices.add(current)
            path = [current]
            while current in cameFrom:
                current = cameFrom[current]
                path.append(current)
            path.reverse()
            return path #Done!

        openVertices.remove(current)
        closedVertices.add(current)
        for neighbour in adjacent(grid,current):
            # print(neighbour)
            if neighbour in closedVertices: 
                continue #We have already processed this node exhaustively
            
            candidateG = G[current] + move_cost(current, neighbour,obstacles)

            if neighbour not in openVertices:
                openVertices.add(neighbour) #Discovered a new vertex
            elif candidateG >= G[neighbour]:
                continue #This G score is worse than previously found

            #Adopt this G score depending on case
            H = manhattan_distance(neighbour,end) 
            if (case == 3):
                cameFrom[neighbour] = current
                G[neighbour] = candidateG                
                F[neighbour] = G[neighbour] + H

            elif (case == 2):
                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                F[neighbour] =  H
            elif (case == 1):
                cameFrom[neighbour] = current
                G[neighbour] = candidateG
                F[neighbour] = G[neighbour]

    
    
    
p = tuple(map(int, input().split()))
f = tuple(map(int, input().split()))
N , M = list(map(int, input().split()))
grid = []
for i in range(0, N):
    grid.append(list(map(str, input())))

path = AStarSearch(grid,p,f,3)
print(len(path)-1)
for i in path:
    print(str(i[0]) + " " + str(i[1]))
    