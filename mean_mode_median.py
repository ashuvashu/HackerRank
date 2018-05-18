'''
This file is for the problem at link
https://www.hackerrank.com/challenges/s10-basic-statistics/problem
'''
import statistics as stats
from collections import Counter

# Next line to take the first input
count = input()

# Next line is to take the input of the list of values
alist = sorted([int(x) for x in input().split()])
adict = dict(Counter(alist))

# Calculating the mean and median
mean = stats.mean(alist)
median = stats.median(alist)

mm = 0
mn = max(alist)

# Trying to check if mode has more than 1 unique values
try:
    mode = stats.mode(alist)
except:
    for j in alist:
        if adict[j] > mm:
            mm = adict[j]
            mode = j


print(mean)
print(median)
print(mode)
