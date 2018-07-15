# Let's get the number of input rows
row_num = int(input())
for i in range(0, row_num):
    row_attrs = input().split(' ')
    try:
        print(int(int(row_attrs[0])//int(row_attrs[1])))
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)