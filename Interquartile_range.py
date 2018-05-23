import statistics as stats
import math
import numpy as np
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
f = []
for i in range(0,len(a)):
    # f = f + np.repeat(a[i], b[i])
    print(np.repeat(a[i], b[i]))
