import numpy as np

#Next line is trick
np.set_printoptions(legacy='1.13')
row_num = [int(x) for x in input().split(' ')]
in_array = []
for i in range(0, row_num[0]):
    in_array.append([int(x) for x in input().split(' ')])

numpy_array = np.array(in_array)
print(np.mean(numpy_array, axis=1))
print(np.var(numpy_array, axis=0))
print(np.std(numpy_array))