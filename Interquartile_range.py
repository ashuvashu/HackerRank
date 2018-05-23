import statistics as stats
import math

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
f = []
for i in range(0,len(a)):
    for j in range(0,b[i]):
        f.append(a[i])

g = sorted(f)

p = stats.median(g[math.ceil(len(g)/2):]) - stats.median(g[0:math.ceil(len(g)/2)])
print(round(float(p),1))
