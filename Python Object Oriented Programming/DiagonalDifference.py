# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:17:29 2022

@author: fsabena
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
arr=[[11,2,4],
     [4,5,6],
     [10,8,-12]]

def diagonalDifference(arr):
    leftdiag=rightdiag=0
    for i in range(n):
        leftdiag += arr[i][i]
        rightdiag += arr[i][n-1-i]
    return abs(leftdiag-rightdiag)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()