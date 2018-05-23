import statistics as stats
import math
import numpy as np
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
f = []
for i in range(0,len(a)):
    f = f + np.repeat(a[i], b[i]).tolist()
    # print(f)
g = sorted(f)
# print(g)
print(stats.median(g[math.ceil(len(g)/2):]) - stats.median(g[0:math.ceil(len(g)/2)]))
