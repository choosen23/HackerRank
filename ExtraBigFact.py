#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    res = [0]*n
    res[0] = 1

    for i in range(1,n):
        res[i] = res[i-1]*(i+1)
   
    print(res[-1])

if __name__ == '__main__':
    n = int(input())
    extraLongFactorials(n)

