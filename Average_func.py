# python3

import math
import os
import random
import re
import sys


def avg(*nums):
    sum= 0
    for n in nums:
        sum = sum+n
    average= sum/len(nums)
    return round(average, 2)

    # write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))
    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()
