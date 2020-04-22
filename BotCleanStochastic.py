#!/bin/python3

import math
def manhattan_distance(p,q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def nextMove(posr, posc, board):
    
    d , b = (0,0) , (posc,posr)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 'd':
                d = (j,i)
                   
    prev = manhattan_distance(b,d)

    """
    sta plaisia tis akisis edw thelei na emfanizw mono tis epomeni kinisi
    me tis dikes m opos tropopoihseis emfanizei oli tin diadromi!!
    """
    
    #GO LEFT    
    if ( manhattan_distance((b[0]-1,b[1]),d) < prev ):
        print("LEFT")       #HACKERRAMK

    #GO RIGHT
    elif ( manhattan_distance((b[0]+1,b[1]),d) < prev ):
        print("RIGHT")  #HACKERRAMK

    #GO UP
    elif ( manhattan_distance((b[0],b[1]-1),d) < prev ):
        print("UP")    #HACKERRAMK
    #GO DOWN
    elif ( manhattan_distance((b[0],b[1]+1),d) < prev ):
        print("DOWN")       #HACKERRAMK
    #CLEAN
    elif ( d == b ):
        print("CLEAN")

    


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
