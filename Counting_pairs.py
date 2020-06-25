# python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
'''def pairs(k, arr):
    count = 0

    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] - arr[j]== k or arr[j] - arr[i]== k:
                count += 1
    return count
'''
def pairs(k, arr):
    d={}
    count=0

    for nums in arr:
        if d.get(nums)==None:
            d[nums]=True

    for nums in arr:
        if d.get(nums+k) == True:
            count+=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
