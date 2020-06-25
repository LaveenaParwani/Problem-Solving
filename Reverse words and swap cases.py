# python3

import math
import os
import random
import re
import sys

# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.


def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')  
  
    # then reverse the split string list and join using space 
    reverse_sentence = ' '.join(reversed(words))  
  
    # finally return the joined string with swapcases
    result = reverse_sentence.swapcase()
    return result
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
