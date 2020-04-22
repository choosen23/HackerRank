#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr) 
	
    arrpos = [*enumerate(arr)] 
    arrpos.sort(key = lambda it:it[1]) 
      
    vis = {k:False for k in range(n)} 
    #krataw se enan grafo to pou einai kathe stixio
    #kai se kathe giro vazw apo 1 stin thesi tou
    #ara to apotelesma tha einai stin xeiroteri o arithmos ton 
    #mi diatetagmenwn stoixwiwn

    ans = 0
    for i in range(n): 
        if vis[i] or arrpos[i][0] == i: 
            continue
        cycle_size = 0
        j = i 
        while not vis[j]: 
            vis[j] = True
            j = arrpos[j][0] 
            cycle_size += 1
              
        if cycle_size > 0: 
            ans += (cycle_size - 1) 
    return ans 


    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

