import re
row_num = int(input())
for i in range(0, row_num):
    re_input = input()
    try:
        re.compile(re_input)
        print(True)
    except Exception as e:
        print(False)