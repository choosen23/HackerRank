
def manhattan_distance(p,q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def nextMove(n,r,c,grid):        
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
    
    """
    sta plaisia tis akisis edw thelei na emfanizw mono tis epomeni kinisi
    me tis dikes m opos tropopoihseis emfanizei oli tin diadromi!!
    """
    if ( manhattan_distance((i-1,j),q) < prev ):
        return "LEFT"       #HACKERRAMK


    if ( manhattan_distance((i+1,j),q) < prev ):
        return "RIGHT"  #HACKERRAMK

    if ( manhattan_distance((i,j-1),q) < prev ):
        return "UP"    #HACKERRAMK
        #GO DOWN

    if ( manhattan_distance((i,j+1),q) < prev ):
        return "DOWN"       #HACKERRAMK


n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))