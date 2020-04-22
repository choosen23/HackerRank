#!/bin/python3

import math
import os
import random
import re
import sys
import array as arr

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds):
    current = 0
    end = n - 1
    jumps = 0
    while current < end:
        if ((current + 2) <= end) and (clouds[current + 2] == 0):
            current += 2
            jumps += 1
        elif clouds[current + 1] == 0:
            current += 1
            jumps += 1
    return jumps 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

