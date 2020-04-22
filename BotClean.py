#!/usr/bin/python

# Head ends here



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
def next_move(posr, posc, board):
    dirties = []
    for i in range(len(board)):
        for j in range(len(board[i])):
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
    
    
    
# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
