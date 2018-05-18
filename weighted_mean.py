'''
This file is for the problem at link
https://www.hackerrank.com/challenges/s10-weighted-mean/problem
'''
# Next line is to take first input
count = int(input())

# Next line is to take from first list of elements
a = [int(x) for x in input().split()]

# Next line is to take from second list of elements
b = [int(x) for x in input().split()]

# Print the output
print(round(sum([a*b for a, b in zip(a, b)])/sum(b),1))
