from itertools import combinations

j = [x for x in input().split()]

parray = []
for i in range(0,int(j[1])):
    parray = parray+list(combinations(sorted(j[0]),i+1))

for k in parray:
    print(''.join(k))
