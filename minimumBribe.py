#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(a):
    
    n = 0
    for i in range(len(q)):
        if q[i] - 1 - i >= 3:
            print("Too chaotic")
            return
    ongoing = True
    last_index = 0
    while ongoing:
        for i in range(last_index, len(q)-1):
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                if i > 0:
                    last_index = i-1
                n += 1
                break
        else:
            ongoing = False
    print(n)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)

