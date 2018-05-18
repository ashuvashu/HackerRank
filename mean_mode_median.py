import math
asize = int(input())
alist = sorted([int(x) for x in input().split()])
mean = sum(alist)/asize
median = (sorted(alist)[math.floor((len(alist)-1)/2)]+sorted(alist)[math.floor((len(alist)-1)/2)])/2
amap = {}
for i in alist:
    if i in amap:
        amap[i] = amap[i]+1
    else:
        amap[i] = 1
a = 0
mode = 0
for i in amap:
    if amap[i] > a:
        a = amap[i]
        mode = i
    else:
        pass
print(mean)
print(mean)
print(mode)
