import numpy

row_num = [int(x) for x in input().split(' ')]
in_array = []
for i in range(0, row_num[0]):
    in_array.append([int(x) for x in input().split(' ')])

numpy_array = numpy.array(in_array)
numpy.set_printoptions(sign=' ')
print(numpy.mean(numpy_array, axis=1))
print(numpy.var(numpy_array, axis=0))
print(numpy.std(numpy_array))