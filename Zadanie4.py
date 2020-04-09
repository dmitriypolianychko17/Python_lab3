import numpy
def matrix(first_row):
    #Wypełniamy matrycę o rozmiarze 5x5 zerami
    array = numpy.zeros((5, 5), dtype=numpy.longlong)
    array[0]=first_row
    for i in range (1,5):
        array[i] = numpy.power(array[i-1], 2)
    return array
first_row = (2,3,4,5,6)
print(matrix(first_row))