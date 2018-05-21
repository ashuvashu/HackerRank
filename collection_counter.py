tot_elem = input()
shoes_set = [int(x) for x in input().split()]
total_val = 0
for i in range(0,int(input())):
    a = [int(x) for x in input().split()]


    if a[0] in shoes_set:
        shoes_set.remove(a[0])
        total_val += a[1]

print(total_val)
