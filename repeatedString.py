#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    string = [str(st) for st in s]
    arxika = string.count('a')
    full = n // len(string)
    half = n % len(string)
    extra = string[:half].count('a')

    return full*arxika + extra


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
