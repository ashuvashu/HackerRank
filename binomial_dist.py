import math

n = 6
x = 3
l = [float(o) for o in input().split()]
p = (l[0]/sum(l))
q = (l[1]/sum(l))

def nCr(n,r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))


sumq = 0
for i in range(x, n+1):
    # print(sumq)
    sumq += nCr(n,i)*(p**i)*((1-p)**(n-i))

print(round(sumq,3))
