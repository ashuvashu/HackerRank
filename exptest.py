from collections import namedtuple
iter = int(input())
stu = namedtuple('stu',input())
a = []
for i in range(iter):
    a.append(int(stu(*input().split()).MARKS))
print(sum(a)/iter)
