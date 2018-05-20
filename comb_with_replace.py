from itertools import combinations_with_replacement
j = input().split()
for i in sorted(list(combinations_with_replacement(j[0], int(j[1])))):
    print(''.join(i))
