'''
This is solution for the problem at
https://www.hackerrank.com/challenges/compress-the-string/problem
'''

from itertools import groupby
a = input()
c = groupby(a)
s = []
for i, j in c:
    print((len(list(j)), int(i)), end=' ')
