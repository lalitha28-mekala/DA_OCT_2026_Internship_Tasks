# Q 4 Funny String
# https://www.hackerrank.com/challenges/funny-string/problem
import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    s_list=[]
    for i in s:
        s_list.append(ord(i))
    r_list = s_list[::-1]
    diff_s=[]
    for j in range(len(s_list)-1):
        diff_s.append(abs(s_list[j]-s_list[(j+1)]))
    diff_r=[]
    for k in range(len(r_list)-1):
        diff_r.append(abs(r_list[k]-r_list[k+1]))
    if diff_r == diff_s:
        return "Funny"
    else:
        return "Not Funny"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
