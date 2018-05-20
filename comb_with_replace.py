from itertools import combinations_with_replacement
j = input().split()
for i in list(combinations_with_replacement(sorted(j[0]), int(j[1]))):
    print(''.join(i))
