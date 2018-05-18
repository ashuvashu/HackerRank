'''
This file is for the problem at link
https://www.hackerrank.com/challenges/s10-quartiles/problem
'''

import statistics as stats
import math

# Next line to take the first input
count = int(input())

# Next line is to take the input of the list of values
alist = sorted([int(x) for x in input().split()])

# Second quartiles
q2 = int(stats.median(alist))


if q2 in alist:
    alist.remove(q2)

# First quartiles
q1list = alist[0:math.floor(len(alist)/2)]

# Third quartiles
q3list = alist[math.ceil(len(alist)/2):]

# Print output
print(int(stats.median(q1list)))
print(q2)
print(int(stats.median(q3list)))
