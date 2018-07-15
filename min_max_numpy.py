import numpy as np

row_num = [int(x) for x in input().split(' ')]
in_array = []
for i in range(0, row_num[0]):
    in_array.append([int(x) for x in input().split(' ')])

numpy_array = np.array(in_array)
print(np.max(np.min(numpy_array, axis=1)))