#!/usr/bin/python




def manhattan_distance(p,q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def displayPathtoPrincess(n,grid):
    #print all the moves here
    q = m = 0
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p':
                q = (j,i)
            elif grid[i][j] == 'm':
                m = (j,i)
     

    prev = manhattan_distance(m,q)
    i = m[0]
    j = m[1]
    

    
    while(prev >= 0 ):
        # print("mpika me apostasi",prev,"eimai sto", m,"kai to point einai ",q)    
        #GO LEFT
        if ( manhattan_distance((i-1,j),q) < prev ):
            prev =  manhattan_distance((i-1,j),q)
            m = (i-1,j)

            print("LEFT")       #choosen23


        #GO RIGHT
        elif ( manhattan_distance((i+1,j),q) < prev ):
            prev = manhattan_distance((i+1,j),q)
            m = (i+1,j)
            print("RIGHT")  #choosen23

        #GO UP
        elif ( manhattan_distance((i,j-1),q) < prev ):
            prev =  manhattan_distance((i,j-1),q)
            m = (i,j-1)
            print("UP")      #choosen23

        #DOWN
        elif ( manhattan_distance((i,j+1),q) < prev ):
            prev =   manhattan_distance((i,j+1),q)
            m = (i,j+1)
            print("DOWN")       #choosen23


        elif ( m == q ):
            break
        i, j = m


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)