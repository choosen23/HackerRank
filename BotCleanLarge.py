
import math
#manhattan_distance
def manhattan_distance(p,q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])

# Find Distance of all dirties
def find_distances(posr, posc, dirties):
    nearest_dirt = []
    for i in dirties:
        # Manhatan Distance distance
        result = manhattan_distance(i,(posr,posc))
        nearest_dirt.append(result)
    return [x for (y,x) in sorted(zip(nearest_dirt,dirties))]

# Set the bot in your new position
def next_move(posx, posy, dimx, dimy, board):
    posr , posc = posx , posy
# def next_move(posr, posc, board):
    dirties = []
    for i in range(dimx):
        for j in range(dimy):
            if board[i][j] == 'd':
                dirties.append([i, j])

    next_dirt = find_distances(posr, posc, dirties)
    if next_dirt[0][1] < posc:
        print('LEFT')
    elif next_dirt[0][1]  > posc:
        print('RIGHT')
    elif next_dirt[0][0] < posr:
        print('UP')
    elif next_dirt[0][0] > posr:
        print('DOWN')
    else:
        print('CLEAN')    
    
    

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
