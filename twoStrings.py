"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Link : https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    string1 = [str(a) for a in s1 ]
    string2 = [str(a) for a in s2]

    set1 = set(string1)
    set2 = set(string2)


    if (set1.intersection(set2)):
        return "YES"
    else:
        return "NO"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
