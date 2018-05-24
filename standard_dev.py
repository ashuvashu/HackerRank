'''
This is silution for the problem at
https://www.hackerrank.com/challenges/s10-standard-deviation/problem
'''
import math
c = int(input())
x = [int(x) for x in input().split()]

def stdev(x):
    lsum = 0
    sqsum = 0
    for i in x:
        lsum += i
    mean = lsum/len(x)

    for i in x:
        sqsum += math.pow((i-mean),2)

    sqmean = math.pow(sqsum/len(x),0.5)
    return sqmean

print(stdev(x))
