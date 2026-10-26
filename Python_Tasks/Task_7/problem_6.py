# Q6 Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s1=s.upper()
    lst=[chr(i) for i in range(ord("A"),ord("Z")+1)]

    for i in lst:
        if  i not in s1:
            return "not pangram"
    else:
        return "pangram"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
