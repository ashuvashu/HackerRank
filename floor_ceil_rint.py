import numpy
#Next Line is tricky part else is easy
numpy.set_printoptions(sign=' ')

in_array = [float(x) for x in input().split(' ')]
num_array = numpy.array(in_array)
print(numpy.floor(num_array))
print(numpy.ceil(num_array))
print(numpy.rint(num_array))